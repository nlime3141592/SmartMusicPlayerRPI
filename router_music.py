from flask import Blueprint

from db import get_cursor

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

    blueprint = Blueprint("music", __name__, url_prefix="/music")

    blueprint.register_blueprint(router_music_info.init())
    blueprint.register_blueprint(router_music_control.init())

    return blueprint