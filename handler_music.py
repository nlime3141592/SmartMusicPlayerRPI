from db import get_cursor
from db import commit

import music

def play_music(id):
    next_music_id = int(id)

    music.set_music_id(next_music_id)
    music_path = "./music/data/" + str(next_music_id) + ".mp3"
    music.play(music_path)

def play_next_music():
    dbCursor = get_cursor()
    dbCursor.execute("select (id) from musiclist where id > ? order by id asc limit 1", [music.get_music_id()])

    next_music_id = -1

    if dbCursor.rowcount > 0: # NOTE: 다음 음악 재생 가능
        row = dbCursor.fetchone()
        next_music_id = int(row[0])
    else:
        dbCursor.execute("select (id) from musiclist order by id asc limit 1")

        if dbCursor.rowcount > 0: # NOTE: 맨 처음 음악 재생 가능
            row = dbCursor.fetchone()
            next_music_id = int(row[0])

    dbCursor.close()

    if next_music_id == -1: # NOTE: 음악을 찾을 수 없음
        pass
    else:
        music.set_music_id(next_music_id)
        music_path = "./music/data/" + str(next_music_id) + ".mp3"
        music.play(music_path)

def play_prev_music():
    dbCursor = get_cursor()
    dbCursor.execute("select (id) from musiclist where id < ? order by id desc limit 1", [music.get_music_id()])

    next_music_id = -1

    if dbCursor.rowcount > 0: # NOTE: 이전 음악 재생 가능
        row = dbCursor.fetchone()
        next_music_id = int(row[0])
    else:
        dbCursor.execute("select (id) from musiclist order by id desc limit 1")

        if dbCursor.rowcount > 0: # NOTE: 맨 끝 음악 재생 가능
            row = dbCursor.fetchone()
            next_music_id = int(row[0])

    dbCursor.close()

    if next_music_id == -1: # NOTE: 음악을 찾을 수 없음
        pass
    else:
        music.set_music_id(next_music_id)
        music_path = "./music/data/" + str(next_music_id) + ".mp3"
        music.play(music_path)

def change_mode_loop():
    dbCursor = get_cursor()
    dbCursor.execute("select (mode_loop) from playerinfo")
    row = dbCursor.fetchone()

    mode_prev = int(row[0])
    mode_next = (mode_prev + 1) % 3
    music.set_mode_loop(mode_next)

    dbCursor.execute("update playerinfo set mode_loop = ?", [mode_next])
    dbCursor.close()

    commit()

def change_mode_shuffle():
    dbCursor = get_cursor()
    dbCursor.execute("select (mode_shuffle) from playerinfo")
    row = dbCursor.fetchone()

    mode_prev = int(row[0])
    mode_next = (mode_prev + 1) % 2
    music.set_mode_shuffle(mode_next)

    dbCursor.execute("update playerinfo set mode_shuffle = ?", [mode_next])
    dbCursor.close()

    commit()

def change_volume_up():
    volume_prev = music.get_volume()
    music.set_volume(volume_prev + 1)
    volume_next = music.get_volume()

    dbCursor = get_cursor()
    dbCursor.execute("update playerinfo set volume = ?", [volume_next])
    dbCursor.close()

    commit()

def change_volume_down():
    volume_prev = music.get_volume()
    music.set_volume(volume_prev - 1)
    volume_next = music.get_volume()

    dbCursor = get_cursor()
    dbCursor.execute("update playerinfo set volume = ?", [volume_next])
    dbCursor.close()

    commit()

def toggle_playing():
    music.toggle_pausing()

def toggle_like(music_id):
    dbCursor = get_cursor()
    dbCursor.execute("select music_like from musiclist where id = ?", [music_id])
    row = dbCursor.fetchone()

    isLike_prev = int(row[0])
    isLike_next = 1 - isLike_prev

    dbCursor.execute("update musiclist set music_like = ? where id = ?", [isLike_next, music_id])
    dbCursor.close()

    commit()

def get_use_ai_detection():
    dbCursor = get_cursor()
    dbCursor.execute("select use_ai_detection from playerinfo")
    row = dbCursor.fetchone()

    dbCursor.close()

    return int(row[0]) != 0

def toggle_ai_detection():
    use_ai_detection = get_use_ai_detection()

    use_ai_detection_prev = 0

    if get_use_ai_detection():
        use_ai_detection_prev = 1

    use_ai_detection_next = 1 - use_ai_detection_prev

    dbCursor = get_cursor()
    dbCursor.execute("update playerinfo set use_ai_detection = ?", [use_ai_detection_next])
    dbCursor.close()

    commit()

def __update_when_music_ends():
    if not music.try_catch_end_event():
        return

    # TODO: 이 곳에 loop 상태, shuffle 상태를 고려한 다음 음악 재생 등의 제어가 필요함.

def update():
    __update_when_music_ends()