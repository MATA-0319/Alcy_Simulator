from pico2d import *

from game_main.config import WIDTH
from game_work import game_framework


# 커서 출력
def cursor_out(self, c):
    if game_framework.mode == 'play':
        # 알키 쓰다듬기 활성화 시 커서가 손으로 변경된다
        if int(WIDTH / 2 - self.alki.size / 3) <= self.m.mx <= int(WIDTH / 2 + self.alki.size / 3) and \
                int(self.alki.head_y + self.alki.size / 50) <= self.m.my <= int(self.alki.head_y + self.alki.size / 4):
            c.cursor_hand.draw(self.x - 35, self.y + 35, 200, 200)
        else:  # 아니라면 기본 커서로 변경
            c.cursor.draw(self.x, self.y, 70, 70)
    else:  # 일시정지 시 기본 커서로 변경
        c.cursor.draw(self.x, self.y, 70, 70)


# 커서 업데이트
def update_cursor(self):
    ts = game_framework.ts
    # 쓰다듬기 실행 시 커서가 좌우로 움직인다
    match game_framework.mode:
        case 'play':
            if self.m.click and self.alki.pat:
                self.x = WIDTH / 2 + math.sin(self.num) * 200
                self.y = self.alki.head_y + self.alki.size / 7
                self.num += ts / 80

            # 종료 시 원래 상태로 초기화
            else:
                self.num = 0
                self.x = self.m.mx + 35
                self.y = self.m.my - 35

            # 커서 위치에 따라 사용할 수 있는 기능이 달라진다
            if int(WIDTH / 2 - self.alki.size / 3) <= self.m.mx <= int(WIDTH / 2 + self.alki.size / 3) and \
                    int(self.alki.head_y + self.alki.size / 50) <= \
                    self.m.my <= int(self.alki.head_y + self.alki.size / 4):
                self.alki.pat = True
            else:
                self.alki.pat = False

        # 일시정지 시 기본 커서 좌표로 변경
        case 'pause':
            self.x = self.m.mx + 35
            self.y = self.m.my - 35
