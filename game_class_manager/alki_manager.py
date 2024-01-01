import math
import random
import time

from pico2d import load_image, load_wav

from game_class_manager.alki_output import middle_out, right_out, left_out
from config import *
from game_mods import play_mode
from game_work import game_framework, game_manager
from ui_class.class_cursor import Cursor


def load_alki_file(a):
    if not a.body:
        a.body = load_image(alki_body)
        a.head_middle = load_image(alki_head_middle)
        a.head_right = load_image(alki_head_right)
        a.head_left = load_image(alki_head_left)

        a.hair = load_image(alki_hair)
        a.tail = load_image(alki_tail)

        a.eye_middle = load_image(alki_eye_middle)
        a.dot_middle = load_image(alki_dot_middle)
        a.brow_middle = load_image(alki_brow_middle)

        a.eye_right = load_image(alki_eye_right)
        a.dot_right = load_image(alki_dot_right)
        a.brow_right = load_image(alki_brow_right)

        a.eye_left = load_image(alki_eye_left)
        a.dot_left = load_image(alki_dot_left)
        a.brow_left = load_image(alki_brow_left)

        a.blink_middle = load_image(alki_blink_middle)
        a.blink_right = load_image(alki_blink_right)
        a.blink_left = load_image(alki_blink_left)

        a.pat_sound = load_wav(pat_sound_file)
        a.pat_sound.set_volume(128)


def init_alki(self, m, e):
    self.m, self.e = m, e  # 마우스 입력

    self.x = WIDTH / 2  # 위치 및 크기, 크기는 화면 길이 가로를 기준으로 설정
    self.y = HEIGHT / 2
    self.size = WIDTH / 10

    self.head_x = WIDTH / 2  # 머리 위치
    self.head_y = self.size / 1.8  # 머리 y 위치는 사이즈를 기준으로 설정된다. 해상도 대응 위함.
    self.state = 'middle'  # 머리 향하는 방향

    self.body_y = 0  # 몸 y좌표
    self.hair_y = 0  # 땋은 머리 y 위치

    self.eye_x, self.eye_y = self.x, self.head_y  # 눈, 눈동자, 눈썹 위치
    self.dot_x, self.dot_y = self.x, self.head_y
    self.brow_x, self.brow_y = self.x, self.head_y

    self.eye_pos_x, self.eye_pos_y = 0, 0  # 추가 움직임 좌표
    self.dot_pos_x, self.dot_pos_y = 0, 0
    self.brow_pos_x, self.brow_pos_y = 0, 0
    self.hair_pos = 0

    self.eye_result_x, self.eye_result_y = 0, 0
    self.dot_result_x, self.dot_reslut_y = 0, 0
    self.brow_result_x, self.brow_result_y = 0, 0
    self.deg_result = 0

    self.start = False  # 게임 시작 시 크기가 커지는 애니메이션 출력
    self.control = False  # 크기가 커지는 애니메이션이 끝나야 컨트롤 가능
    self.blink = False  # 눈 깜빡임 여부
    self.time_measure = False  # 시간 측정 여부

    self.pat = False  # 쓰다듬을 수 있는 여부

    self.deg_head = 0  # 최종 각도
    self.deg_tail = 0

    self.num_head = 0  # 삼각함수 변수
    self.num_tail = 0
    self.num_hair = 0

    self.pause_acc = 0  # 일시정지 전환 시 사용하는 가속값

    self.pat_sound_delay = 0  # 사운드 재생 딜레이


# 게임 시작 애니에미션
def start_animation(self):
    ts = game_framework.ts

    if self.start:
        if self.size < WIDTH / 2:
            prev_size = self.size
            self.size += ts * 2
            self.head_y += (self.size - prev_size) / 1.8

            self.eye_y, self.dot_y, self.brow_y = self.head_y, self.head_y, self.head_y

            if self.size > WIDTH / 2:
                self.size = WIDTH / 2
                self.head_y += (self.size - prev_size) / 1.8
                self.eye_y, self.dot_y, self.brow_y = self.head_y, self.head_y, self.head_y

                cursor = Cursor(play_mode.mouse_input, play_mode.alki)
                game_manager.add_object(cursor, 7)  # 커서가 나타난다

                self.start = False
                self.m.input = True  # 마우스 입력을 받기 시작한다


# 마우스 위치에 따라 바라보는 방향이 달라진다
def set_state(self):
    if self.m.mx >= WIDTH / 2 + self.size / 2:
        self.state = 'right'
    elif self.m.mx <= WIDTH / 2 - self.size / 2:
        self.state = 'left'
    else:
        self.state = 'middle'


# 보는 방향이 바뀌었을 때 머리가 부드럽게 움직인다
def head_animation(self):
    ts = game_framework.ts

    # 방향 전환 시 해당 방향으로 머리가 움직인다
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
    self.eye_pos_y = (self.m.my - self.eye_y) / 15
    self.dot_pos_x = (self.m.mx - self.dot_x) / 15
    self.dot_pos_y = (self.m.my - self.dot_y) / 10
    self.brow_pos_y = (self.m.my - self.brow_y) / 25
    # print(self.dot_pos_y, self.eye_pos_y, self.m.my)

    # 특정 값 이상 움직이면 더 이상 움직이지 않도록 한다.
    if self.eye_pos_x > WIDTH / 70:
        self.eye_pos_x = WIDTH / 70
    elif self.eye_pos_x < -WIDTH / 70:
        self.eye_pos_x = -WIDTH / 70

    if self.dot_pos_x > WIDTH / 50:
        self.dot_pos_x = WIDTH / 50
    elif self.dot_pos_x < -WIDTH / 50:
        self.dot_pos_x = -WIDTH / 50

    if self.eye_pos_y > HEIGHT / 45:
        self.eye_pos_y = HEIGHT / 45
    elif self.eye_pos_y < -HEIGHT / 45:
        self.eye_pos_y = -HEIGHT / 45

    if self.dot_pos_y > HEIGHT / 25:
        self.dot_pos_y = HEIGHT / 25
    elif self.dot_pos_y < -HEIGHT / 25:
        self.dot_pos_y = -HEIGHT / 25


# 눈 깜빡임 업데이트
def update_blink(self):
    global prev_time, rand_time

    # 시간 측정 시작
    if not self.time_measure:
        prev_time = time.time()
        rand_time = random.randint(1, 4)  # 눈 깜빡임 간격 랜덤 설정
        self.time_measure = True

    # 설정된 시간이 되면 눈을 감거나 뜬다
    if self.time_measure:
        cur_time = time.time() - prev_time
        if self.blink:  # 눈이 감긴 상태에서는 0.2초 후 다시 눈을 뜬다
            if cur_time >= 0.2:
                self.blink = False
                self.time_measre = False
        else:  # 눈이 떠 있는 상태에서는 설정된 시간이 되면 눈을 감는다
            if cur_time >= rand_time:
                self.blink = True
                self.time_measure = False


# 쓰다듬기 업데이트
def update_pat(self, a):
    ts = game_framework.ts
    self.num_head += ts / 80
    self.num_hair += ts / 80
    self.num_tail += ts / 200

    self.deg_tail = math.sin(self.num_tail) * 200  # 꼬리 회전
    self.deg_head = -math.sin(self.num_head) * 200  # 머리 회전
    self.hair_pos = math.sin(self.num_hair) * 200  # 머리카락 상하 이동

    # 쓰다듬기 사운드 재생
    self.pat_sound_delay -= ts / 10
    if self.pat_sound_delay <= 0:
        a.pat_sound.play(1)
        self.pat_sound_delay = 50


# 쓰다듬기 관련 변수 초기화
def init_deg(self, a):
    if not self.m.click:
        self.pat_sound_delay = 0
        self.deg_head, self.num_head, self.deg_tail, self.num_tail = 0, 0, 0, 0  # 쓰다듬기 안 하면 초기화
        self.num_hair, self.hair_pos = 0, 0


# 일시정지 복귀 애니메이션
def pause_resume_alki(self):
    ts = game_framework.ts

    match game_framework.mode:
        case 'pause':
            self.head_y += self.pause_acc * ts
            self.body_y += self.pause_acc * ts
            self.hair_y += self.pause_acc * ts

            self.pause_acc -= ts / 20

            if self.pause_acc < 0:
                self.pause_acc = 0

        case 'play':
            self.head_y -= self.pause_acc * ts
            self.body_y -= self.pause_acc * ts
            self.hair_y -= self.pause_acc * ts

            self.pause_acc -= ts / 20

            if self.pause_acc < 0:
                self.pause_acc = 0


def update_result(self):
    self.eye_result_x = self.eye_x + self.eye_pos_x + self.e.ex  # 마우스 좌표, 카메라, 고정 좌표를 더한 최종 값
    self.eye_result_y = self.eye_y + self.eye_pos_y + self.e.ey
    self.dot_result_x = self.dot_x + self.dot_pos_x + self.e.ex
    self.dot_result_y = self.dot_y + self.dot_pos_y + self.e.ey
    self.brow_result_x = self.brow_x + self.e.ex
    self.brow_result_y = self.brow_y + self.brow_pos_y + self.e.ey
    self.deg_result = math.radians(self.deg_head) / 40  # 이미지 회전 각도


# 알키 출력
def output(self, a):
    # 꼬리 출력
    a.tail.rotate_draw(math.radians(self.deg_tail) / 30, self.x - (self.size / 4) + self.e.ex,
                       self.body_y + self.e.ey, self.size, self.size)
    # 몸 출력
    a.body.rotate_draw(-math.radians(self.deg_head) / 100, self.x + self.e.ex,
                       self.body_y + self.e.ey, self.size, self.size)
    # 머리카락 출력
    a.hair.rotate_draw(0, self.x + self.e.ex, self.hair_pos / 10 + self.e.ey + self.hair_y,
                       self.size, self.size)

    # 바라보는 방향에 따라 다른 이미지를 출력
    match self.state:
        case 'middle': middle_out(self, a)
        case 'right': right_out(self, a)
        case 'left': left_out(self, a)

