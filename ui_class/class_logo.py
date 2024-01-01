import time

from pico2d import*

from config import *
from game_work import game_framework, game_manager


class StartLogo:
    image = None

    def __init__(self):
        if not StartLogo.image:
            StartLogo.background = load_image(start_background_image)
            StartLogo.mata_logo = load_image(mata_logo_image)

        self.op = 1
        self.prev_time = time.time()
        self.cur_time = 0

    def draw(self):
        StartLogo.background.opacify(self.op)
        StartLogo.mata_logo.opacify(self.op)
        StartLogo.background.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        StartLogo.mata_logo.draw(WIDTH / 2, HEIGHT / 2, HEIGHT / 2, HEIGHT / 2)

    def update(self):
        ts = game_framework.ts

        self.cur_time = time.time() - self.prev_time
        if self.cur_time > 2:
            self.op -= ts / 400
            if self.op <= 0:
                self.op = 0
                # 로고 출력이 끝나면 시작이 가능해진다
                game_framework.start_enable = True
                game_manager.remove_object(self)


class Logo:
    image = None

    def __init__(self):
        if not Logo.image:
            Logo.image = load_image(logo_image)
            Logo.font = load_font(font, 50)
            Logo.start_sound = load_wav(start_sound_file)
            Logo.start_sound.set_volume(48)

        self.size = HEIGHT
        self.title_out = True
        self.fadeout = False
        self.press_out = True
        self.play_start_sound = False
        self.op = 1
        self.op_press = 1

    def draw(self):
        if self.title_out:
            if self.press_out:
                self.font.draw(WIDTH / 2 - 140, HEIGHT / 2 - 300, 'Press SPACE', (255, 255, 255))
            Logo.image.opacify(self.op)
            Logo.image.draw(WIDTH / 2, HEIGHT / 2, self.size, self.size)

    def update(self):
        ts = game_framework.ts
        if self.play_start_sound:
            Logo.start_sound.play(1)
            self.play_start_sound = False

        if self.fadeout:
            self.press_out = False
            self.size += ts * 2
            self.op -= ts / 200
            if self.op < 0:
                self.op = 0
                game_manager.remove_object(self)
