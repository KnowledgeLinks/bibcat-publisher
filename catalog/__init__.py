__author__ = "Jeremy Nelson"

from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")
google_login_blprt = make_google_blueprint(
    client_id=app.config.get("GOOGLE_CLIENT_ID"),
    client_secret=app.config.GOOGLE_CLIENT_SECRET,
    scope=["profile", "email"])

app.register_blueprint(google_login_blprt, url_prefix="/login")



