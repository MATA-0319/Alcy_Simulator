from game_class.alki_manager import set_state, move_eye, head_animation, output, init_alki, start_animation, blink, \
    update_pat, init_deg
from game_class.file_loader import load_alki_file
from game_main.config import *
from pico2d import *

from game_work import game_framework


class Alki:
    body = None

    def __init__(self, m, e):
        load_alki_file(Alki)
        init_alki(self, m, e)

    def draw(self):
        output(self, Alki)

    def update(self):
        blink(self)

        if self.start:
            start_animation(self)

        if self.m.input:
            set_state(self)
            head_animation(self)
            move_eye(self)

        if self.pat and self.m.click:
            update_pat(self)

        init_deg(self)
