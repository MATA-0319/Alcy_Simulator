from pico2d import *

from game_class.file_loader import load_background_file
from game_main.config import *
from game_mods import play_mode
from game_work import game_framework


class Background:
    image = None

    def __init__(self, e):
        load_background_file(Background)

        self.e = e
        self.x, self.y = WIDTH / 2, HEIGHT / 2
        self.size_x, self.size_y = WIDTH, HEIGHT

    def draw(self):
        Background.image.draw(WIDTH / 2 + self.e.ex, HEIGHT / 2 + self.e.ey, self.size_x, self.size_y)

    def update(self):
        ts = game_framework.ts
        if play_mode.alki.start:
            self.size_x += ts * 2
            self.size_y += ts * 2
            if self.size_x > WIDTH * 1.5:
                self.size_x = WIDTH * 1.5
                self.size_y = HEIGHT * 1.5
