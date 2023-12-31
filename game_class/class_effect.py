from game_main.config import *
from game_mods import play_mode


#  화면 효과 클래스
class Effect:
    def __init__(self, m):
        self.m = m
        self.cam_x = 0
        self.cam_y = 0
        self.ex, self.ey = 0, 0

    def draw(self):
        pass

    def update(self):
        self.cam_x = (WIDTH / 2 - self.m.mx) / 10
        self.cam_y = (HEIGHT / 2 - self.m.my) / 10

        # 효과 추가 시 아래의 식에 더하여 일괄 처리한다
        if self.m.input:
            self.ex = self.cam_x
            self.ey = self.cam_y
