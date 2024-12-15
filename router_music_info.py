from flask import Blueprint
from flask import Response

from db import get_cursor
from db import commit

import music

def init():

    blueprint = Blueprint("info", __name__, url_prefix="/info")

    @blueprint.route("/volume", methods=["GET"])
    def next():
        dbCursor = get_cursor()
        dbCursor.execute("select (volume) from playerinfo")
        row = dbCursor.fetchone()
        dbCursor.close()

        volume_int = int(row[0])

        print("VOLUME을 얻었습니다. (%d)" % (volume_int))
        return Response(status=204)

    return blueprint