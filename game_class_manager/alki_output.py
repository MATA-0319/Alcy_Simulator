from pico2d import *

from game_work import game_framework


# 앞쪽 방향 출력
def middle_out(self, a):
    if self.m.click and self.pat and game_framework.mode == 'play':  # 쓰다듬을 때는 눈을 감는다
        a.head_middle.rotate_draw(self.deg_result, self.head_x + self.e.ex, self.head_y + self.e.ey,
                                  self.size, self.size)
        a.blink_middle.rotate_draw(self.deg_result, self.eye_result_x, self.eye_result_y, self.size, self.size)
        a.brow_middle.rotate_draw(self.deg_result, self.brow_result_x, self.brow_result_y, self.size, self.size)

    else:
        a.head_middle.rotate_draw(0, self.head_x + self.e.ex, self.head_y + self.e.ey, self.size, self.size)
        if self.blink:
            a.blink_middle.rotate_draw(0, self.eye_result_x, self.eye_result_y, self.size, self.size)
        else:
            a.eye_middle.rotate_draw(0, self.eye_result_x, self.eye_result_y, self.size, self.size)
            a.dot_middle.rotate_draw(0, self.dot_result_x, self.dot_result_y, self.size, self.size)
        a.brow_middle.rotate_draw(0, self.brow_result_x, self.brow_result_y, self.size, self.size)


# 오른쪽 방향 출력
def right_out(self, a):
    a.head_right.rotate_draw(0, self.head_x + self.e.ex, self.head_y + self.e.ey, self.size, self.size)
    if self.blink:
        a.blink_right.rotate_draw(0, self.eye_result_x, self.eye_result_y, self.size, self.size)
    else:
        a.eye_right.rotate_draw(0, self.eye_result_x, self.eye_result_y, self.size, self.size)
        a.dot_right.rotate_draw(0, self.dot_result_x, self.dot_result_y, self.size, self.size)
    a.brow_right.rotate_draw(0, self.brow_result_x, self.brow_result_y, self.size, self.size)


# 왼쪽 방향 출력
def left_out(self, a):
    a.head_left.rotate_draw(0, self.head_x + self.e.ex, self.head_y + self.e.ey, self.size, self.size)
    if self.blink:
        a.blink_left.rotate_draw(0, self.eye_result_x, self.eye_result_y, self.size, self.size)
    else:
        a.eye_left.rotate_draw(0, self.eye_result_x, self.eye_result_y, self.size, self.size)
        a.dot_left.rotate_draw(0, self.dot_result_x, self.dot_result_y, self.size, self.size)
    a.brow_left.rotate_draw(0, self.brow_result_x, self.brow_result_y, self.size, self.size)
