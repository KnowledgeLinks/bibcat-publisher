import pkg_resources
import click
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from flask import abort, flash, jsonify, redirect, render_template 
from flask import request, url_for
from flask_dance.contrib.google import google
from flask_dance.contrib.facebook import facebook
from .forms import LoginForm
#try:
#    es = Elasticsearch(
#        current_app.config.get("ELASTICSEARCH", "localhost"))
#except:
es = Elasticsearch()

def internal_server_error(e):
    return render_template("500.html", error=e), 500

def search_data():
    output_format, output = "html", []
    if request.method.startswith("POST"):
        query_phrase = request.form.get("query", "")
        offset = request.form.get("offset", 0)
    else:
        query_phrase = request.args.get("query", "")
        offset = request.args.get("offset", 0)
    search = Search(using=es)
    search = search.query(
        Q("query_string", 
          query=query_phrase,
          default_operator="AND")).params(size=4, 
              from_=offset)
    results = search.execute()
    if output_format.startswith("json"):
        return jsonify(output)
    return render_template("search-results.html",
        results=results,
        offset=offset,
        query_phrase=query_phrase)


def suggest(name=None):
    if not name:
        return
    query = request.args.get("q")
    name = name.lower()
    search = Search(using=es)
    if name.startswith("work"):
        search = search.query(
            Q("match", value=query)).source(include=["value"])
    results = search.execute() 
    soup = BeautifulSoup('', 'lxml')
    output = soup.new_tag("div", 
        style="padding: 1em 2m; width: 700px", 
        **{"class": "row bg-white"})
    work_div = soup.new_tag("div",
        **{"class": "col-4"})
    work_title = soup.new_tag("h3")
    work_title.string = "Works ({:,})".format(results.hits.total)
    work_div.append(work_title)
    work_list = soup.new_tag("ol")
    for row in results.hits.hits:
        li = soup.new_tag("li")
        link = soup.new_tag("a", 
            href="{}.html".format(row.get("_id")))
        link.string = row.get("_source").get("value")
        li.append(link)
        work_list.append(li)
    work_div.append(work_list)
    output.append(work_div)
    people_search = Search(using=es)
    people_search = people_search.query(
        Q("match", **{"bf_hasInstance.bf_contribution.value": query}))\
        .source(include=["bf_hasInstance.bf_contribution.value", "value"])
    people_results = people_search.execute() 
    people_div = soup.new_tag("div",
        **{"class": "col-4"})
    people_title = soup.new_tag("h3")
    people_title.string = "People & Organizations ({:,})".format(
        people_results.hits.total)
    people_div.append(people_title)
    for row in people_results.hits.hits:
        for instance in row.get("_source").get("bf_hasInstance"):
            contribution = instance.get("bf_contribution")
            if not isinstance(contribution, list):
                contribution = [contribution, ]
            for contributor in contribution:
                span = soup.new_tag("span")
                span.string = "{} in ".format(
                    contributor.get("value")[0:150])
                link = soup.new_tag("a",
                    href="{}.html".format(row.get("_id")))
                link.string = row.get("_source").get("value")[0:150]
                span.append(link)
                people_div.append(span)
    output.append(people_div)
    subject_search = Search(using=es)
    subject_search = subject_search.query(
        Q("match", **{"bf_subject.value": query}))\
        .source(include=["bf_subject.value", "value"])
    subject_results = subject_search.execute()
    subject_div = soup.new_tag("div",
        **{"class": "col-4"})
    subject_title = soup.new_tag("h3")
    subject_title.string="Subjects ({:,})".format(subject_results.hits.total)
    subject_div.append(subject_title)
    for hit in subject_results.hits.hits:
        for subject in hit.get('_source').get("bf_subject"):
            if isinstance(subject, str):
                subject = {"value": subject}
            span = soup.new_tag("span")
            span.string = "{} in ".format(
                subject.get("value"))
            link = soup.new_tag("a",
                href="{}.html".format(row.get("_id")))
            link.string = row.get("_source").get("value")
            span.append(link)
            subject_div.append(span)
    output.append(subject_div)
    return jsonify({"html": output.prettify()})



def profile(service=None):
    if service.endswith("google"):
        if not google.authorized:
            return redirect(url_for("google.login"))
        resp = google.get("/oauth2/v2/userinfo")
        assert resp.ok, resp.text
        return "Your Google {email}".format(email=resp.json()["email"])
    elif service.endswith("facebook"):
        if not facebook.authorized:
            return redirect(url_for("facebook.login"))
        resp = facebook.get("/oauth2/v2/userinfo")
        assert resp.ok, resp.text
        return "Your Facebook Authorization and {email}".format(
            email=resp.json()["email"])
    else:
        return render_template("profile.html")
    return abort(404)

def publisher_login():
    login_form = LoginForm()
#    if request.method.startswith("POST"):
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        return redirect("profile")
    return render_template("login.html", form=login_form)

def into_list(data):
    if isinstance(data, dict):
        return [data, ]
    elif isinstance(data, list):
        return data

def home():
    flash("Public Message")
    return render_template("index.html")
