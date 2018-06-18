__author__ = "Jeremy Nelson"

from flask import Flask, redirect, url_for
from flask_dance.contrib.facebook import make_facebook_blueprint
from flask_dance.contrib.google import make_google_blueprint

from rdfframework.configuration import RdfConfigManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")
config_mgr = RdfConfigManager(app.config, verify=False)
data_connection = config_mgr.conns

facebook_login_blueprint = make_facebook_blueprint(
    client_id=app.config.get("FACEBOOK_CLIENT_ID"),
    client_secret=app.config.get("FACEBOOK_CLIENT_SECRET"))

google_login_blueprint = make_google_blueprint(
    client_id=app.config.get("GOOGLE_CLIENT_ID"),
    client_secret=app.config.get("GOOGLE_CLIENT_SECRET"),
    scope=["profile", "email"])

app.register_blueprint(facebook_login_blueprint, url_prefix="/login-facebook")
app.register_blueprint(google_login_blueprint, url_prefix="/login-google")

from .api import catalog
app.register_blueprint(catalog)

from .views import home

@app.route("/")
def app_home():
    return home()
