from game_class.alki_manager import set_state, move_eye, head_animation, output, init_alki
from game_class.file_loader import load_alki_file
from game_main.config import *
from pico2d import *

from game_work import game_framework


class Alki:
    head_middle, head_right, head_left, body = None, None, None, None
    eye_middle, dot_middle, brow_middle = None, None, None
    eye_right, dot_right, brow_right = None, None, None
    eye_left, dot_left, brow_left = None, None, None
    hair = None
    tail = None

    def __init__(self, m, e):
        load_alki_file(Alki)
        init_alki(self, m, e)

    def draw(self):
        output(self, Alki)

    def update(self):
        set_state(self)
        head_animation(self)
        move_eye(self)
