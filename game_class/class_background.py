from pico2d import *

from game_main.config import *
from game_mods import play_mode
from game_work import game_framework


class Background:
    image = None

    def __init__(self, e):
        if not Background.image:
            Background.image = load_image(background_image)

        self.e = e
        self.x, self.y = WIDTH / 2, HEIGHT / 2
        self.size_x, self.size_y = WIDTH, HEIGHT
        self.acc = 0

    def draw(self):
        Background.image.draw(self.x + self.e.ex, self.y + self.e.ey, self.size_x, self.size_y)

    def update(self):
        ts = game_framework.ts

        if play_mode.alki.start:
            self.size_x += ts * 2
            self.size_y += ts * 2
            if self.size_x > WIDTH * 1.5:
                self.size_x = WIDTH * 1.5
                self.size_y = HEIGHT * 1.5

        match game_framework.mode:
            case 'pause':
                self.y += self.acc * ts
                self.acc -= ts / 20
                if self.acc < 0:
                    self.acc = 0

            case 'play':
                self.y -= self.acc * ts
                self.acc -= ts / 20
                if self.acc < 0:
                    self.acc = 0
