import pkg_resources

from flask import abort, flash, jsonify, render_template, request
from flask_dance.contrib.google import google
from . import app

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
    return abort(404)


@app.route("/")
def home():
    flash("Public Message")
    return render_template("index.html")
