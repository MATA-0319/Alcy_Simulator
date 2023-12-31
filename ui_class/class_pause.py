from pico2d import *
from game_main.config import *
from game_work import game_framework


class Pause:
    back = None

    def __init__(self, m):
        if not Pause.back:
            Pause.back = load_image(pause_back)
            Pause.icon_exit = load_image(icon_exit_image)
            Pause.button = load_image(pause_button_image)

        self.m = m

        self.x = WIDTH / 2
        self.y = -150
        self.acc = 0
        self.button_left = [WIDTH - i * 150 - 150 for i in range(1, 3)]
        self.button_right = [WIDTH - i * 150 + 150 for i in range(1, 3)]
        self.button_pos = [WIDTH - i * 150 for i in range(1, 3)]
        self.button_on = [False for i in range(1, 3)]

    def draw(self):
        Pause.back.draw(self.x, self.y, WIDTH, 300)
        Pause.icon_exit.draw(WIDTH - 130, self.y + 10, 150, 150)

        if self.button_on[0]:
            Pause.button.draw(self.button_pos[0], self.y, 300, 300)

    def update(self):
        ts = game_framework.ts

        if self.button_left[0] < self.m.mx < self.button_right[0] and self.m.my < self.y + 150:
            self.button_on[0] = True
            if self.m.click:
                game_framework.stop_run()

        else:
            self.button_on[0] = False

        match game_framework.mode:
            case 'pause':
                self.y += self.acc * ts
                self.acc -= ts / 20
                if self.acc < 0:
                    self.acc = 0

            case 'play':
                self.y -= self.acc * ts
                self.acc -= ts / 20
                if self.acc < 0:
                    self.acc = 0
