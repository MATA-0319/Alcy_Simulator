from pico2d import *

from game_class_manager.background_manager import start_animation_bg, pause_resume_bg
from config import *


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
        start_animation_bg(self)
        pause_resume_bg(self)


