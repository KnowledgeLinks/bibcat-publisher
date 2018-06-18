__author__ = "Jeremy Nelson", "Mike Stabile", "Jay Peterson"

from flask import Blueprint, render_template
#import views
from .views import search_data as search_catalog
from .views import into_list as to_list
from .views import publisher_login, suggest

catalog = Blueprint('catalog', __name__,
                template_folder='templates')

@catalog.app_template_filter("/into_list")
def into_list(entity):
    return to_list(entity)

@catalog.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", error=e), 500


@catalog.route("/detail")
def record_detail():
    return "In record detail"

@catalog.route("/search", methods=["GET", "POST"])
def search_data():
    #return views.search_data()
    return search_catalog()

@catalog.route("/suggest/<path:name>")
def auto_suggest(name=None):
    return suggest(name)

@catalog.route("/login")
def publisher_login():
    return publisher_login()
