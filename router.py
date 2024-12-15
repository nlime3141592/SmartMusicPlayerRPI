import db

from flask import Blueprint
from flask import render_template

import router_music

def init():
    blueprint = Blueprint("root", __name__, url_prefix="")

    @blueprint.route("/")
    def render_page():
        return render_template("./index.html")

    blueprint.register_blueprint(router_music.init())

    return blueprint