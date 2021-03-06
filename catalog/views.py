import pkg_resources

from flask import jsonify, render_template, request
from . import app

@app.route("/search", methods=["GET", "POST"])
def search_data():
    if request.method.startswith("POST"):
        query_terms = request.form.get("query")
        output = {"results": [], "query": query_terms }
    else:
        query_terms = request.args.get("query")
        output = {"results": [], "query": query_terms}
    print("Args: {} Output: {}".format(request.args, output))
    return jsonify(output)

@app.route("/detail")
def detail():
    return render_template("detail.html")

@app.route("/")
def home():
    return render_template("index.html")
