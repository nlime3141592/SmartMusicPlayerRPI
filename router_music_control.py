from flask import Blueprint
from flask import Response

from db import get_cursor
from db import commit

import music
import handler_music

def init():

    blueprint = Blueprint("control", __name__, url_prefix="/control")

    @blueprint.route("/next", methods=["POST"])
    def next():
        handler_music.play_next_music()
        print("NEXT를 수신했습니다.")
        return Response(status=204)

    @blueprint.route("/prev", methods=["POST"])
    def prev():
        handler_music.play_prev_music()
        print("PREV를 수신했습니다.")
        return Response(status=204)

    @blueprint.route("/change_loop", methods=["POST"])
    def change_loop():
        handler_music.change_mode_loop()
        print("TOGGLE LOOP를 수신했습니다.")
        return Response(status=204)

    @blueprint.route("/change_shuffle", methods=["POST"])
    def change_shuffle():
        handler_music.change_mode_shuffle()
        print("CHANGE SHUFFLE을 수신했습니다.")
        return Response(status=204)

    @blueprint.route("/toggle_like/<id>", methods=["POST"])
    def toggle_like(id):
        dbCursor = get_cursor()
        dbCursor.execute("select music_like from musiclist where id = ?", [id])
        row = dbCursor.fetchone()
        dbCursor.close()

        isLike = int(row[0])
        dbCursor = get_cursor()
        dbCursor.execute("update musiclist set music_like = ? where id = ?", [1 - isLike, id])
        dbCursor.close()

        commit()
        print("TOGGLE LIKE를 수신했습니다.")

        return Response(status=204)

    @blueprint.route("/volup", methods=["POST"])
    def volup():
        handler_music.change_volume_up()
        print("VOLUP을 수신했습니다.")
        return Response(status=204)

    @blueprint.route("/voldown", methods=["POST"])
    def voldown():
        handler_music.change_volume_down()
        print("VOLDOWN을 수신했습니다.")
        return Response(status=204)

    @blueprint.route("/volmute", methods=["POST"])
    def volmute():
        print("VOLMUTE를 수신했습니다.")
        return Response(status=204)

    @blueprint.route("/toggle_playing", methods=["POST"])
    def toggle_playing():
        handler_music.toggle_playing()
        print("TOGGLE PLAYING을 수신했습니다.")
        return Response(status=204)

    @blueprint.route("/toggle_ai", methods=["POST"])
    def toggle_ai():
        print("TOGGLE AI를 수신했습니다.")
        return Response(status=204)

    return blueprint