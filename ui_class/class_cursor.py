from pico2d import *

from config import cursor_image, cursor_hand_image
from ui_class_manager.cursor_manager import update_cursor, cursor_out


class Cursor:
    cursor = None

    def __init__(self, m, alki):
        if not Cursor.cursor:
            Cursor.cursor = load_image(cursor_image)
            Cursor.cursor_hand = load_image(cursor_hand_image)

        self.m, self.alki = m, alki
        self.num = 0
        self.x, self.y = 0, 0

    def draw(self):
        cursor_out(self, Cursor)

    def update(self):
        update_cursor(self)
