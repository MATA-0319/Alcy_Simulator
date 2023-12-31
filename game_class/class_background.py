from pico2d import *

from game_class.file_loader import load_background_file
from game_main.config import *


class Background:
    image = None

    def __init__(self, e):
        load_background_file(Background)

        self.e = e
        self.x, self.y = WIDTH / 2, HEIGHT / 2

    def draw(self):
        Background.image.draw(WIDTH / 2 + self.e.ex, HEIGHT / 2 + self.e.ey, WIDTH * 1.5, HEIGHT * 1.5)

    def update(self):
        pass
