from pico2d import *

from game_class.file_loader import load_cursor_file
from game_main.config import WIDTH
import math

from game_work import game_framework


class Cursor:
    cursor = None

    def __init__(self, m, alki):
        load_cursor_file(Cursor)

        self.m, self.alki = m, alki
        self.num = 0
        self.x, self.y = 0, 0

    def draw(self):
        if int(WIDTH / 2 - self.alki.size / 3) <= self.m.mx <= int(WIDTH / 2 + self.alki.size / 3) and \
                int(self.alki.head_y + 100) <= self.m.my <= int(self.alki.head_y + 300):
            Cursor.cursor_hand.draw(self.x - 35, self.y + 35, 200, 200)
            self.alki.pat = True
        else:
            self.alki.pat = False
            Cursor.cursor.draw(self.x, self.y, 70, 70)

    def update(self):
        ts = game_framework.ts
        if self.m.click and self.alki.pat:
            self.x = WIDTH / 2 + math.sin(self.num) * 200
            self.y = self.alki.head_y + 200
            self.num += ts / 80
        else:
            self.num = 0
            self.x = self.m.mx + 35
            self.y = self.m.my - 35
