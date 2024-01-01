from config import *
from game_mods import play_mode
from game_work import game_framework


# 일시정지 버튼 출력
def pause_button_out(self, p):
    # 게임 시작 후에 일시정지 버튼을 보이도록 한다
    if play_mode.mouse_input.input:
        if self.menu_on:
            p.menu_button.draw(self.menu_pos, self.y + 250, 450, 200)
        p.font.draw(WIDTH - 380, self.y + 150 + 85, 'ESC', (255, 255, 255))
        p.icon_pause.draw(WIDTH - 110, self.y + 150 + 95, 150, 150)


# 일시정지 메뉴 출력
def pause_out(self, p):
    p.back.draw(self.x, self.y, WIDTH, 300)

    for i in range(2):
        if self.button_on[i]:
            p.button.draw(self.button_pos[i], self.y, 300, 300)

    p.icon_exit.draw(self.button_pos[0] + 20, self.y + 10, 150, 150)
    p.icon_info.draw(self.button_pos[1], self.y + 15, 150, 150)


# 정보 출력
def info_out(self, p):
    if self.info:
        p.font2.draw(20, self.y + 100, 'Alcyone Simulator by MATA_', (255, 255, 255))
        p.font2.draw(20, self.y + 60, 'Indev 0.1', (255, 255, 255))
        p.font2.draw(20, self.y + 20, 'Powered by Pico 2d', (255, 255, 255))


# 일시정지 버튼 업데이트
def update_pause_button(self, p):
    if self.menu_left < self.m.mx < self.menu_right and self.y + 150 < self.m.my < self.y + 350:
        self.menu_on = True  # 범위 안에 커서 감지 시 버튼 표시

        if self.m.click:
            p.button_click.play()
            pause_resume_clk()  # 마우스 클릭 시 일시정지 또는 복귀
            self.m.click = False
    else:  # 범위를 벗어나면 버튼 표시 안 함
        self.menu_on = False


# 일시정지 메뉴 업데이트
def update_pause(self, p):
    for i in range(2):
        if self.button_left[i] < self.m.mx < self.button_right[i] and self.m.my < self.y + 150:
            self.button_on[i] = True  # 버튼 범위 안에 커서가 감지되면 해당 버튼이 표시된다

            if self.m.click:  # 클릭 시 기능 사용 가능
                match i:
                    case 0: game_framework.stop_run()  # 게임 종료
                    case 1:
                        p.button_click.play()  # 버튼 소리 재생
                        if not self.info:  # 정보를 표시하거나 끈다
                            self.info = True
                        elif self.info:
                            self.info = False
                self.m.click = False  # 클릭하면 다시 클릭 비활성화

        else:  # 위치가 벗어나면 버튼이 표시되지 않는다
            self.button_on[i] = False


# 일시정지 메뉴 애니메이션
def pause_animation(self):
    ts = game_framework.ts

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


# 일시정지, 복귀 애니메이션
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
            