from pico2d import *

from game_main.config import *
from game_mods import play_mode
from game_work import game_framework


def pause_resume_clk():
    match game_framework.mode:
        case 'play':
            play_mode.alki.pause_acc = 5
            play_mode.alki.head_y = play_mode.alki.size / 1.8
            play_mode.alki.body_y = 0
            play_mode.alki.hair_y = 0

            play_mode.background.acc = 5
            play_mode.background.y = HEIGHT / 2

            play_mode.pause.acc = 5
            play_mode.pause.y = -150
            play_mode.mouse_input.click = False

            game_framework.mode = 'pause'

        case 'pause':
            play_mode.alki.pause_acc = 5
            play_mode.alki.head_y = play_mode.alki.size / 1.8 + 252
            play_mode.alki.body_y = 252
            play_mode.alki.hair_y = 252

            play_mode.background.acc = 5
            play_mode.background.y = HEIGHT / 2 + 252

            play_mode.pause.acc = 5
            play_mode.pause.y = 102

            game_framework.mode = 'play'


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

            Pause.font = load_font(font, 100)
            Pause.font2 = load_font(font, 40)

        self.m = m

        self.x = WIDTH / 2
        self.y = -150
        self.acc = 0
        self.button_pos = [WIDTH - 150 - i * 300 for i in range(2)]
        self.button_left = [self.button_pos[i] - 150 for i in range(2)]
        self.button_right = [self.button_pos[i] + 150 for i in range(2)]
        self.button_on = [False for i in range(2)]

        self.menu_left = WIDTH - 500
        self.menu_right = WIDTH
        self.menu_pos = WIDTH - 250
        self.menu_on = False

        self.info = False

    def draw(self):
        if play_mode.mouse_input.input:
            if self.menu_on:
                Pause.menu_button.draw(self.menu_pos, self.y + 250, 500, 200)
            Pause.font.draw(WIDTH - 380, self.y + 150 + 85, 'ESC', (255, 255, 255))
            Pause.icon_pause.draw(WIDTH - 110, self.y + 150 + 95, 150, 150)

        Pause.back.draw(self.x, self.y, WIDTH, 300)

        for i in range(2):
            if self.button_on[i]:
                Pause.button.draw(self.button_pos[i], self.y, 300, 300)

        Pause.icon_exit.draw(self.button_pos[0] + 20, self.y + 10, 150, 150)
        Pause.icon_info.draw(self.button_pos[1], self.y + 15, 150, 150)

        if self.info:
            Pause.font2.draw(20, self.y + 100, 'Alcyone Simulator by MATA_', (255, 255, 255))
            Pause.font2.draw(20, self.y + 60, 'Alpha 0.1', (255, 255, 255))
            Pause.font2.draw(20, self.y + 20, 'Powered by Pico 2d', (255, 255, 255))

    def update(self):
        ts = game_framework.ts

        for i in range(2):
            if self.button_left[i] < self.m.mx < self.button_right[i] and self.m.my < self.y + 150:
                self.button_on[i] = True
                if self.m.click:
                    if i == 0:
                        game_framework.stop_run()
                    elif i == 1:
                        if not self.info:
                            self.info = True
                        elif self.info:
                            self.info = False

                    self.m.click = False

            else:
                self.button_on[i] = False

        if self.menu_left < self.m.mx < self.menu_right and self.y + 150 < self.m.my < self.y + 350:
            self.menu_on = True
            if self.m.click:
                pause_resume_clk()
                self.m.click = False
        else:
            self.menu_on = False

        match game_framework.mode:
            case 'pause':
                self.y += self.acc * ts
                self.acc -= ts / 20
                if self.acc < 0:
                    self.acc = 0

            case 'play':
                self.info = False
                self.y -= self.acc * ts
                self.acc -= ts / 20
                if self.acc < 0:
                    self.acc = 0
