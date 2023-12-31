from game_class.class_cursor import Cursor
from game_main.config import *
import math
import time
import random

from game_mods import play_mode
from game_work import game_framework, game_manager


def init_alki(self, m, e):
    self.m, self.e = m, e  # 마우스 입력

    self.x = WIDTH / 2  # 위치 및 크기, 크기는 화면 길이 가로를 기준으로 설정
    self.y = HEIGHT / 2
    self.size = WIDTH / 10

    self.head_x = WIDTH / 2  # 머리 위치
    self.head_y = self.size / 1.8

    self.eye_x, self.eye_y = self.x, self.head_y  # 눈, 눈동자, 눈썹 위치
    self.dot_x, self.dot_y = self.x, self.head_y
    self.brow_x, self.brow_y = self.x, self.head_y
    self.hair_y = 0  # 땋은 머리 위치

    self.eye_pos_x, self.eye_pos_y = 0, 0  # 추가 움직임 좌표
    self.dot_pos_x, self.dot_pos_y = 0, 0
    self.brow_pos_x, self.brow_pos_y = 0, 0

    self.state = 'middle'  # 머리 향하는 방향

    self.start = False  # 게임 시작 시 크기가 커지는 애니메이션 출력
    self.control = False  # 크기가 커지는 애니메이션이 끝나야 컨트롤 가능
    self.blink = False  # 눈 깜빡임 여부
    self.time_measure = False  # 시간 측정 여부


def start_animation(self):
    ts = game_framework.ts
    if self.size < WIDTH / 2:
        prev_size = self.size
        self.size += ts * 2
        self.head_y += (self.size - prev_size) / 1.8

        self.eye_y, self.dot_y, self.brow_y = self.head_y, self.head_y, self.head_y

        if self.size > WIDTH / 2:
            self.size = WIDTH / 2
            self.head_y += (self.size - prev_size) / 1.8
            self.eye_y, self.dot_y, self.brow_y = self.head_y, self.head_y, self.head_y

            cursor = Cursor(play_mode.mouse_input)
            game_manager.add_object(cursor, 7)  # 커서가 나타난다

            self.start = False
            self.m.input = True  # 마우스 입력을 받기 시작한다


# 마우스 위치에 따라 바라보는 방향이 달라진다
def set_state(self):
    if self.m.mx >= WIDTH / 2 + self.size / 3:
        self.state = 'right'
    elif self.m.mx <= WIDTH / 2 - self.size / 3:
        self.state = 'left'
    else:
        self.state = 'middle'


# 보는 방향이 바뀌었을 때 머리가 부드럽게 움직인다
def head_animation(self):
    ts = game_framework.ts

    match self.state:
        case 'right':
            if self.head_x < WIDTH / 2 + 70:
                self.head_x += ts
                if self.head_x > WIDTH / 2 + 70:
                    self.head_x = WIDTH / 2 + 70
        case 'left':
            if self.head_x > WIDTH / 2 - 70:
                self.head_x -= ts
                if self.head_x < WIDTH / 2 - 70:
                    self.head_x = WIDTH / 2 - 70

        case 'middle':
            if self.head_x < WIDTH / 2:
                self.head_x += ts
                if self.head_x > WIDTH / 2:
                    self.head_x = WIDTH / 2

            if self.head_x > WIDTH / 2:
                self.head_x -= ts
                if self.head_x < WIDTH / 2:
                    self.head_x = WIDTH / 2


# 눈은 항상 마우스를 따라 본다
def move_eye(self):
    # 눈 좌표는 항상 머리 좌표를 기준으로 설정된다
    self.eye_x, self.dot_x, self.brow_x = self.head_x, self.head_x, self.head_x
    self.eye_y, self.dot_y, self.brow_y = self.head_y, self.head_y, self.head_y

    #  알키는 마우스를 따라 본다
    self.eye_pos_x = (self.m.mx - self.eye_x) / 20
    self.eye_pos_y = (self.m.my - self.eye_y) / 18
    self.dot_pos_x = (self.m.mx - self.dot_x) / 15
    self.dot_pos_y = (self.m.my - self.dot_y) / 13
    self.brow_pos_y = (self.m.my - self.brow_y) / 25
    # print(self.dot_pos_x, self.eye_pos_x, self.m.mx)

    if self.eye_pos_x > WIDTH / 60:
        self.eye_pos_x = WIDTH / 60
    elif self.eye_pos_x < -WIDTH / 60:
        self.eye_pos_x = -WIDTH / 60

    if self.dot_pos_x > WIDTH / 40:
        self.dot_pos_x = WIDTH / 40
    elif self.dot_pos_x < -WIDTH / 40:
        self.dot_pos_x = -WIDTH / 40


def blink(self):
    global prev_time, rand_time

    if not self.time_measure:
        prev_time = time.time()
        rand_time = random.randint(1, 4)
        self.time_measure = True

    if self.time_measure:
        cur_time = time.time() - prev_time
        if not self.blink:
            if cur_time >= rand_time:
                self.blink = True
                self.time_measure = False
        else:
            if cur_time >= 0.2:
                self.blink = False
                self.time_measre = False


# 알키 출력
def output(self, a):
    a.tail.rotate_draw(0, self.x - (self.size / 4) + self.e.ex, self.e.ey, self.size, self.size)
    a.body.rotate_draw(0, self.x + self.e.ex, self.e.ey, self.size, self.size)
    a.hair.rotate_draw(0, self.x + self.e.ex, self.hair_y + self.e.ey, self.size, self.size)

    eye_result_x = self.eye_x + self.eye_pos_x + self.e.ex
    eye_result_y = self.eye_y + self.eye_pos_y + self.e.ey
    dot_result_x = self.dot_x + self.dot_pos_x + self.e.ex
    dot_result_y = self.dot_y + self.dot_pos_y + self.e.ey
    brow_result_x = self.brow_x + self.e.ex
    brow_result_y = self.brow_y + self.brow_pos_y + self.e.ey

    match self.state:
        case 'middle':
            a.head_middle.rotate_draw(0, self.head_x + self.e.ex, self.head_y + self.e.ey, self.size, self.size)
            if not self.blink:
                a.eye_middle.rotate_draw(0, eye_result_x, eye_result_y, self.size, self.size)
                a.dot_middle.rotate_draw(0, dot_result_x, dot_result_y, self.size, self.size)
            else:
                a.blink_middle.rotate_draw(0, eye_result_x, eye_result_y, self.size, self.size)
            a.brow_middle.rotate_draw(0, brow_result_x, brow_result_y, self.size, self.size)

        case 'right':
            a.head_right.rotate_draw(0, self.head_x + self.e.ex, self.head_y + self.e.ey, self.size, self.size)
            if not self.blink:
                a.eye_right.rotate_draw(0, eye_result_x, eye_result_y, self.size, self.size)
                a.dot_right.rotate_draw(0, dot_result_x, dot_result_y, self.size, self.size)
            else:
                a.blink_right.rotate_draw(0, eye_result_x, eye_result_y, self.size, self.size)
            a.brow_right.rotate_draw(0, brow_result_x, brow_result_y, self.size, self.size)

        case 'left':
            a.head_left.rotate_draw(0, self.head_x + self.e.ex, self.head_y + self.e.ey, self.size, self.size)
            if not self.blink:
                a.eye_left.rotate_draw(0, eye_result_x, eye_result_y, self.size, self.size)
                a.dot_left.rotate_draw(0, dot_result_x, dot_result_y, self.size, self.size)
            else:
                a.blink_left.rotate_draw(0, eye_result_x, eye_result_y, self.size, self.size)
            a.brow_left.rotate_draw(0, brow_result_x, brow_result_y, self.size, self.size)
