import pygame

# NOTE: Event codes.
c_MUSIC_END_EVENT = 100

# NOTE: Loop states.
c_MODE_NO_LOOP = 0
c_MODE_LOOP_LIST = 1
c_MODE_LOOP_MUSIC = 2

# NOTE: Shuffle states.
c_MODE_NO_SHUFFLE = 0
c_MODE_SHUFFLE = 1

c_VOLUME_MAX = 15
c_VOLUME_MIN = 0

__is_playing = False
__is_pausing = True
__position_pausing = 0

__music_id = 0

__mode_loop = c_MODE_NO_LOOP
__mode_shuffle = c_MODE_NO_SHUFFLE

__volume_int = (c_VOLUME_MAX + c_VOLUME_MIN) // 2

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_endevent(c_MUSIC_END_EVENT)

def try_catch_end_event():
    for event in pygame.event.get():
        if event.type == c_MUSIC_END_EVENT:
            return True
    return False

def set_volume(volume_int):
    global c_VOLUME_MAX
    global c_VOLUME_MIN
    global __volume_int

    if volume_int > c_VOLUME_MAX:
        __volume_int = c_VOLUME_MAX
    elif volume_int < c_VOLUME_MIN:
        __volume_int = c_VOLUME_MIN
    else:
        __volume_int = volume_int

    dv0 = c_VOLUME_MAX - c_VOLUME_MIN
    dv1 = __volume_int - c_VOLUME_MIN
    volume01 = dv1 / dv0

    pygame.mixer.music.set_volume(volume01)

def get_volume():
    global __volume_int
    return __volume_int

def play_begin():
    global __is_playing
    global __is_pausing
    global __volume_int

    set_volume(__volume_int)
    pygame.mixer.music.play()
    __is_pausing = False
    __is_playing = True

def play(path):
    pygame.mixer.music.load(path)
    play_begin()

def set_music_id(music_id):
    global __music_id

    __music_id = music_id

def get_music_id():
    global __music_id

    return __music_id

def toggle_pausing():
    global __is_pausing
    global __position_pausing

    __is_pausing = (__is_pausing == False)

    if __is_pausing:
        __position_pausing = pygame.mixer.music.get_pos() / 1000.0
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.play(start=__position_pausing)

def set_mode_loop(mode):
    global __mode_loop
    __mode_loop = mode

def get_mode_loop():
    global __mode_loop
    return __mode_loop

def set_mode_shuffle(mode):
    global __mode_shuffle
    __mode_shuffle = mode

def get_mode_shuffle():
    global __mode_shuffle
    return __mode_shuffle

def init(init_music_id, init_mode_loop, init_mode_shuffle, init_volume):
    global __music_id

    __music_id = init_music_id
    set_mode_loop(init_mode_loop)
    set_mode_shuffle(init_mode_shuffle)
    set_volume(init_volume)

if __name__ == "__main__":
    import time
    play("./music/data/3.mp3")
    time.sleep(5)
    toggle_pausing()
    time.sleep(5)
    toggle_pausing()
    time.sleep(5)
    set_volume(6)
    time.sleep(5)
    toggle_pausing()
    time.sleep(5)
    toggle_pausing()
    time.sleep(5)
    set_volume(4)
    time.sleep(5)
    set_volume(1)
    time.sleep(5)
    set_volume(9)
    time.sleep(5)
    print("ok")