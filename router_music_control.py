from flask import Blueprint
from flask import Response

from db import get_cursor
from db import commit

import music
import handler_music

def init():

    blueprint = Blueprint("control", __name__, url_prefix="/control")

    @blueprint.route("/play/<id>", methods=["POST"])
    def play_id(id):
        handler_music.play_music(id)
        return Response(status=204)

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

    # TODO: music_id를 URI에 포함하여 기능을 사용하는 테스트가 필요함.
    @blueprint.route("/toggle_like/<music_id>", methods=["POST"])
    def toggle_like(music_id):
        handler_music.toggle_like(int(music_id))
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

    # NOTE: Front-End에서 버튼을 빠른 속도로 클릭할 때 음악 재생이 처음부터 다시 시작하는 오류 현상을 발견함.
    # TODO: music.toggle_pausing() 함수 및 음악 재생/정지 제어 관련 로직의 구조 점검이 필요함.
    @blueprint.route("/toggle_playing", methods=["POST"])
    def toggle_playing():
        handler_music.toggle_playing()
        print("TOGGLE PLAYING을 수신했습니다.")
        return Response(status=204)

    @blueprint.route("/toggle_ai", methods=["POST"])
    def toggle_ai():
        handler_music.toggle_ai_detection()
        print("TOGGLE AI를 수신했습니다.")
        return Response(status=204)

    return blueprint