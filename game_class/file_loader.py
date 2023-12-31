from pico2d import *

from game_main.config import *


def load_alki_file(a):
    if not a.body:
        a.body = load_image(alki_body)
        a.head_middle = load_image(alki_head_middle)
        a.head_right = load_image(alki_head_right)
        a.head_left = load_image(alki_head_left)

        a.eye_middle = load_image(alki_eye_middle)
        a.dot_middle = load_image(alki_dot_middle)
        a.brow_middle = load_image(alki_brow_middle)
