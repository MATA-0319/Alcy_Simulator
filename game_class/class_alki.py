from game_class.file_loader import load_alki_file
from game_main.config import *
from pico2d import *


class Alki:
    head_middle, head_right, head_left, body = None, None, None, None
    eye_middle, dot_middle, brow_middle = None, None, None
    eye_right, dot_right, brow_right = None, None, None
    eye_left, dot_left, brow_left = None, None, None
    hair = None
    tail = None

    def __init__(self, m, e):
        load_alki_file(Alki)

        self.m, self.e = m, e  # 마우스 입력

        self.x = WIDTH / 2  # 위치 및 크기, 크기는 화면 길이 가로를 기준으로 설정
        self.y = HEIGHT / 2
        self.size = WIDTH / 2

        self.eye_x, self.eye_y = self.x, self.y  # 눈, 눈동자, 눈썹 위치
        self.dot_x, self.dot_y = self.x, self.y
        self.brow_x, self.brow_y = self.x, self.y
        self.hair_y = self.y - 700

        self.state = 'middle'  # 머리 향하는 방향

    def draw(self):
        global ex, ey, eye_pos_x, eye_pos_y, dot_pos_x, dot_pos_y, brow_pos_x, brow_pos_y

        Alki.tail.rotate_draw(0, self.x - 300 + ex, self.y - 700 + ey, self.size, self.size)
        Alki.body.rotate_draw(0, self.x + ex, self.y - 700 + ey, self.size, self.size)  # 사이즈는 화면 가로 길이를 기준으로 정함
        Alki.hair.rotate_draw(0, self.x + ex, self.hair_y + ey, self.size, self.size)

        match self.state:
            case 'middle':
                Alki.head_middle.rotate_draw(0, self.x + ex, self.y + ey, self.size, self.size)
                Alki.eye_middle.rotate_draw(0, self.eye_x + eye_pos_x + ex, self.eye_y + eye_pos_y + ey, self.size, self.size)
                Alki.dot_middle.rotate_draw(0, self.dot_x + dot_pos_x + ex, self.dot_y + dot_pos_y + ey, self.size, self.size)
                Alki.brow_middle.rotate_draw(0, self.brow_x + ex, self.brow_y + brow_pos_y + ey, self.size, self.size)

            case 'right':
                Alki.head_right.rotate_draw(0, self.x + 50 + ex, self.y + ey, self.size, self.size)
                Alki.eye_right.rotate_draw(0, self.eye_x + 50 + eye_pos_x + ex, self.eye_y + eye_pos_y + ey, self.size, self.size)
                Alki.dot_right.rotate_draw(0, self.dot_x + 50 + dot_pos_x + ex, self.dot_y + dot_pos_y + ey, self.size, self.size)
                Alki.brow_right.rotate_draw(0, self.brow_x + 50 + ex, self.brow_y + brow_pos_y + ey, self.size, self.size)

            case 'left':
                Alki.head_left.rotate_draw(0, self.x - 50 + ex, self.y + ey, self.size, self.size)
                Alki.eye_left.rotate_draw(0, self.eye_x - 50 + eye_pos_x + ex, self.eye_y + eye_pos_y + ey, self.size, self.size)
                Alki.dot_left.rotate_draw(0, self.dot_x - 50 + dot_pos_x + ex, self.dot_y + dot_pos_y + ey, self.size, self.size)
                Alki.brow_left.rotate_draw(0, self.brow_x - 50 + ex, self.brow_y + brow_pos_y + ey, self.size, self.size)

    def update(self):
        global ex, ey, eye_pos_x, eye_pos_y, dot_pos_x, dot_pos_y, brow_pos_x, brow_pos_y

        # 마우스 위치에 따라 바라보는 방향이 달라진다
        if self.m.x >= self.x + 700:
            self.state = 'right'
        elif self.m.x <= self.x - 700:
            self.state = 'left'
        else:
            self.state = 'middle'

        # 화면 효과
        ex = self.e.ex
        ey = self.e.ey

        #  알키는 마우스를 따라 본다
        eye_pos_x = (self.m.x - self.eye_x) / 30
        eye_pos_y = (self.m.y - self.eye_y) / 30
        dot_pos_x = (self.m.x - self.dot_x) / 20
        dot_pos_y = (self.m.y - self.dot_y) / 20

        # 눈이 특정 높이 이상 올라가면 눈썹이 같이 올라간다
        if eye_pos_y >= 10:
            brow_pos_y = eye_pos_y - 10
        else:
            brow_pos_y = 0

        # 알키의 모든 부분은 하나의 좌표로 통일된다
        self.eye_x, self.eye_y = self.x, self.y  # 눈, 눈동자, 눈썹 위치
        self.dot_x, self.dot_y = self.x, self.y
        self.brow_x, self.brow_y = self.x, self.y
        self.hair_y = self.y - 700
