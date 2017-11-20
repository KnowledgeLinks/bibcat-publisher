import pkg_resources

from . import app

@app.route("/")
def home():
    return "BIBCAT Publisher"
