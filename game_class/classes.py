from game_main.config import *
from pico2d import *


class Alki:
    head_middle, head_right, head_left, body = None, None, None, None

    def __init__(self):
        if not Alki.body:
            Alki.body = load_image(alki_body)
            Alki.head_middle = load_image(alki_head_middle)
            Alki.head_right = load_image(alki_head_right)
            Alki.head_left = load_image(alki_head_left)

        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.state = 'middle'  # 머리 향하는 방향

    def draw(self):
        Alki.body.rotate_draw(0, self.x, self.y - 700, WIDTH / 2, WIDTH / 2)  # 사이즈는 화면 가로 길이를 기준으로 정함
        match self.state:
            case 'middle':
                Alki.head_middle.rotate_draw(0, self.x, self.y, WIDTH / 2, WIDTH / 2)
            case 'right':
                Alki.head_right.rotate_draw(0, self.x + 50, self.y, WIDTH / 2, WIDTH / 2)
            case 'left':
                Alki.head_left.rotate_draw(0, self.x - 50, self.y, WIDTH / 2, WIDTH / 2)

    def update(self):
        pass


