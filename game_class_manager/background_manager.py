from config import WIDTH, HEIGHT
from game_mods import play_mode
from game_work import game_framework


def pause_resume_bg(self):
    ts = game_framework.ts

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


def start_animation_bg(self):
    ts = game_framework.ts

    if play_mode.alki.start:
        self.size_x += ts * 2
        self.size_y += ts * 2
        if self.size_x > WIDTH * 1.5:
            self.size_x = WIDTH * 1.5
            self.size_y = HEIGHT * 1.5
