__author__ = "Jeremy Nelson"

from flask import Flask, redirect, url_for
from flask_dance.contrib.facebook import make_facebook_blueprint
from flask_dance.contrib.google import make_google_blueprint

from rdfframework.configuration import RdfConfigManager

catalog = Flask(__name__, instance_relative_config=True)
catalog.config.from_pyfile("config.py")
config_mgr = RdfConfigManager(catalog.config, verify=False)
data_connection = config_mgr.conns

facebook_login_blueprint = make_facebook_blueprint(
    client_id=catalog.config.get("FACEBOOK_CLIENT_ID"),
    client_secret=catalog.config.get("FACEBOOK_CLIENT_SECRET"))

google_login_blueprint = make_google_blueprint(
    client_id=catalog.config.get("GOOGLE_CLIENT_ID"),
    client_secret=catalog.config.get("GOOGLE_CLIENT_SECRET"),
    scope=["profile", "email"])

catalog.register_blueprint(facebook_login_blueprint, url_prefix="/login-facebook")
catalog.register_blueprint(google_login_blueprint, url_prefix="/login-google")

from .views import detail, home, profile, search_data, suggest
from .views import publisher_login as base_login

@catalog.template_filter("/into_list")
def into_list(entity):
    return into_list(entity)

@catalog.route("/detail")
def app_detail():
    return detail()

@catalog.route("/profile/<path:service>")
def app_profile(service=None):
    return profile(service)

@catalog.route("/login")
def publisher_login():
    return base_login()
 
@catalog.route("/search", methods=["GET", "POST"])
def search_data():
    return search_data

@catalog.route("/suggest/<path:name>")
def app_suggest(name=None):
    return suggest(name)

@catalog.route("/")
def app_home():
    return home()
