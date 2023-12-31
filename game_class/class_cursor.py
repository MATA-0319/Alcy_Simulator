from pico2d import *

from game_class.file_loader import load_cursor_file


class Cursor:
    image = None

    def __init__(self, m):
        load_cursor_file(Cursor)

        self.m = m
        self.x, self.y = 0, 0

    def draw(self):
        Cursor.image.draw(self.x, self.y, 70, 70)

    def update(self):
        self.x = self.m.mx + 35
        self.y = self.m.my - 35
