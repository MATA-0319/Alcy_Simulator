from game_class.file_loader import load_alki_file
from game_main.config import *
from pico2d import *


class Alki:
    head_middle, head_right, head_left, body = None, None, None, None
    eye_middle, dot_middle, brow_middle = None, None, None

    def __init__(self, m):
        load_alki_file(Alki)

        self.m = m  # 마우스 입력

        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.size = WIDTH / 2

        self.eye_x, self.eye_y = WIDTH / 2, HEIGHT / 2
        self.dot_x, self.dot_y = WIDTH / 2, HEIGHT / 2
        self.brow_x, self.brow_y = WIDTH / 2, HEIGHT / 2

        self.state = 'middle'  # 머리 향하는 방향

    def draw(self):
        eye_pos_x = (self.m.x - self.eye_x) / 25
        eye_pos_y = (self.m.y - self.eye_y) / 25
        dot_pos_x = (self.m.x - self.dot_x) / 20
        dot_pos_y = (self.m.y - self.dot_y) / 20

        if eye_pos_y >= 10:
            brow_pos_y = eye_pos_y - 15
        else:
            brow_pos_y = 0

        Alki.body.rotate_draw(0, self.x, self.y - 700, WIDTH / 2, WIDTH / 2)  # 사이즈는 화면 가로 길이를 기준으로 정함
        match self.state:
            case 'middle':
                Alki.head_middle.rotate_draw(0, self.x, self.y, self.size, self.size)
                Alki.eye_middle.rotate_draw(0, self.eye_x + eye_pos_x, self.eye_y + eye_pos_y, self.size, self.size)
                Alki.dot_middle.rotate_draw(0, self.dot_x + dot_pos_x, self.dot_y + dot_pos_y, self.size, self.size)
                Alki.brow_middle.rotate_draw(0, self.brow_x, self.brow_y + brow_pos_y, self.size, self.size)
            case 'right':
                Alki.head_right.rotate_draw(0, self.x + 50, self.y, self.size, self.size)
            case 'left':
                Alki.head_left.rotate_draw(0, self.x - 50, self.y, self.size, self.size)

    def update(self):
        pass


