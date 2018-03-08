import pkg_resources

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from flask import abort, flash, jsonify, redirect, render_template 
from flask import request, url_for
from flask_dance.contrib.google import google
from flask_dance.contrib.facebook import facebook
from . import app, config_mgr, data_connection
from .forms import LoginForm
 

es = Elasticsearch()

@app.route("/search", methods=["GET", "POST"])
def search_data():
    output_format, output = "html", []
    if request.method.startswith("POST"):
        query_phrase = request.form.get("query")
        offset = request.form.get("offset", 0)
    else:
        query_phrase = request.args.get("query")
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

@app.route("/suggest")
def suggest():
    query = request.args.get("query")
    creator_search = Search(using=es)
    work_search = Search(using=es)
    subject_search = Search(using=es)
    return "<div>Answer</div>"


@app.route("/detail")
def detail():
    return render_template("detail.html")

@app.route("/profile/<path:service>")
def profile(service=None):
    if service.endswith("google"):
        if not google.authorized:
            return redirect(url_for("google.login"))
        resp = google.get("/oauth2/v2/userinfo")
        assert resp.ok, resp.text
        print(resp.json())
        return "Your Google {email}".format(email=resp.json()["email"])
    elif service.endswith("facebook"):
        if not facebook.authorized:
            return redirect(url_for("facebook.login"))
        resp = facebook.get("/oauth2/v2/userinfo")
        assert resp.ok, resp.text
        print(resp.json())
        return "Your Facebook Authorization and {email}".format(
            email=resp.json()["email"])
    else:
        return render_template("profile.html")
    return abort(404)

@app.route("/login", methods=['POST', 'GET'])
def publisher_login():
    login_form = LoginForm()
#    if request.method.startswith("POST"):
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        return redirect("profile")
    return render_template("login.html", form=login_form)
   

@app.route("/")
def home():
    flash("Public Message")
    return render_template("index.html")
