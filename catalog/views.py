import pkg_resources

from flask import abort, flash, jsonify, redirect, render_template 
from flask import request, url_for
from flask_dance.contrib.google import google
from flask_dance.contrib.facebook import facebook
from . import app
from .forms import LoginForm

@app.route("/search", methods=["GET", "POST"])
def search_data():
    if request.method.startswith("POST"):
        query_terms = request.form.get("query")
        output = {"results": [], "query": query_terms }
    else:
        query_terms = request.args.get("query")
        output = {"results": [], "query": query_terms}
    return jsonify(output)

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
