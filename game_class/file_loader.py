from pico2d import *

from game_main.config import *


def load_alki_file(a):
    if not a.body:
        a.body = load_image(alki_body)
        a.head_middle = load_image(alki_head_middle)
        a.head_right = load_image(alki_head_right)
        a.head_left = load_image(alki_head_left)

        a.hair = load_image(alki_hair)
        a.tail = load_image(alki_tail)

        a.eye_middle = load_image(alki_eye_middle)
        a.dot_middle = load_image(alki_dot_middle)
        a.brow_middle = load_image(alki_brow_middle)

        a.eye_right = load_image(alki_eye_right)
        a.dot_right = load_image(alki_dot_right)
        a.brow_right = load_image(alki_brow_right)

        a.eye_left = load_image(alki_eye_left)
        a.dot_left = load_image(alki_dot_left)
        a.brow_left = load_image(alki_brow_left)

        a.blink_middle = load_image(alki_blink_middle)
        a.blink_right = load_image(alki_blink_right)
        a.blink_left = load_image(alki_blink_left)


def load_background_file(a):
    if not a.image:
        a.image = load_image(background_image)


def load_cursor_file(a):
    if not a.cursor:
        a.cursor = load_image(cursor_image)
        a.cursor_hand = load_image(cursor_hand_image)
