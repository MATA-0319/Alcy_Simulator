from pico2d import *

from game_main.config import *
from ui_class_manager.menu_manager import pause_button_out, pause_out, info_out, update_pause_button, \
    update_pause, pause_animation


class Pause:
    back = None

    def __init__(self, m):
        if not Pause.back:
            Pause.back = load_image(pause_back)
            Pause.icon_pause = load_image(icon_pause_image)
            Pause.icon_exit = load_image(icon_exit_image)
            Pause.icon_info = load_image(icon_info_image)

            Pause.button = load_image(pause_button_image)
            Pause.menu_button = load_image(menu_button_image)
            Pause.button_click = load_wav(button_click_sound)

            Pause.font = load_font(font, 100)
            Pause.font2 = load_font(font, 40)

        self.m = m  # 마우스 좌표

        self.x = WIDTH / 2  # 배경 위치
        self.y = -150
        self.acc = 0  # 가속값

        # 버튼 위치, 좌우 좌표
        self.button_pos = [WIDTH - 150 - i * 300 for i in range(2)]
        self.button_left = [self.button_pos[i] - 150 for i in range(2)]
        self.button_right = [self.button_pos[i] + 150 for i in range(2)]
        self.button_on = [False for i in range(2)]

        # 일시정지 버튼 위치, 좌표
        self.menu_left = WIDTH - 500
        self.menu_right = WIDTH
        self.menu_pos = WIDTH - 250
        self.menu_on = False

        # 정보 출력 여부
        self.info = False

    def draw(self):
        pause_button_out(self, Pause)
        pause_out(self, Pause)
        info_out(self, Pause)

    def update(self):
        update_pause_button(self, Pause)
        update_pause(self, Pause)
        pause_animation(self)
