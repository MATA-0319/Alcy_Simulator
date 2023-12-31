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
        # 커서 위치에 따라 커서 형태가 달라진다
        if int(WIDTH / 2 - self.alki.size / 3) <= self.m.mx <= int(WIDTH / 2 + self.alki.size / 3) and \
                int(self.alki.head_y + self.alki.size / 50) <= self.m.my <= int(self.alki.head_y + self.alki.size / 4):
            Cursor.cursor_hand.draw(self.x - 35, self.y + 35, 200, 200)
        else:
            Cursor.cursor.draw(self.x, self.y, 70, 70)

    def update(self):
        ts = game_framework.ts

        # 쓰다듬기 실행 시 커서가 좌우로 움직인다
        if self.m.click and self.alki.pat:
            self.x = WIDTH / 2 + math.sin(self.num) * 200
            self.y = self.alki.head_y + self.alki.size / 7
            self.num += ts / 80

        # 종료 시 원래 상태로 초기화
        else:
            self.num = 0
            self.x = self.m.mx + 35
            self.y = self.m.my - 35

        # 커서 위치에 따라 사용할 수 있는 기능이 달라진다
        if int(WIDTH / 2 - self.alki.size / 3) <= self.m.mx <= int(WIDTH / 2 + self.alki.size / 3) and \
                int(self.alki.head_y + self.alki.size / 50) <= self.m.my <= int(self.alki.head_y + self.alki.size / 4):
            self.alki.pat = True
        else:
            self.alki.pat = False
