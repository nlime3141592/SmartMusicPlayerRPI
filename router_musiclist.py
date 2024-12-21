from flask import Blueprint
from flask import render_template

from db import get_cursor
from db import commit

import json

import music
import router_music_info
import router_music_control

def __init_music():
    dbCursor = get_cursor()

    dbCursor.execute("select * from playerinfo")
    row = dbCursor.fetchone()
    dbCursor.close()

    music_id = int(row[0])
    mode_loop = int(row[1])
    mode_shuffle = int(row[2])
    volume_int = int(row[3])

    music.init(music_id, mode_loop, mode_shuffle, volume_int)

def init():

    __init_music()

    blueprint = Blueprint("musiclist", __name__, url_prefix="/musiclist")

    @blueprint.route("/", methods=["GET"])
    def page_musiclist():
        return render_template("./musiclist.html")

    @blueprint.route("/reload", methods=["GET"])
    def reload():
        commit()
        dbCursor = get_cursor()
        dbCursor.execute("select id, music_name, artists, upload_date from musiclist")
        results = dbCursor.fetchall()
        dbCursor.close()

        if results == None:
            return "[]"
        else:
            jsonString = json.dumps(results, indent=4, sort_keys=True, default=str)
            return jsonString

    @blueprint.route("/delete/<id>", methods=["POST"])
    def delete_id(id):
        dbCursor = get_cursor()
        dbCursor.execute(f"delete from musiclist where id = {id}")
        dbCursor.close
        commit()

        return ""

    blueprint.register_blueprint(router_music_info.init())
    blueprint.register_blueprint(router_music_control.init())

    return blueprint