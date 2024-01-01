from pico2d import *

from game_class.class_alki import Alki
from game_class.class_background import Background
from config import *
from game_work import game_manager, game_framework
from ui_class.class_effect import Effect
from ui_class.class_logo import Logo, StartLogo
from ui_class.class_mouse_input import MouseInput
from ui_class.class_pause import Pause


def pause_resume_esc():
    global mouse_input, alki, background, pause

    match game_framework.mode:
        case 'play':  # to pause
            alki.pause_acc = 5
            alki.head_y = alki.size / 1.8
            alki.body_y = 0
            alki.hair_y = 0

            background.acc = 5
            background.y = HEIGHT / 2

            pause.acc = 5
            pause.y = -150
            mouse_input.click = False

            game_framework.mode = 'pause'

        case 'pause':  # to play
            alki.pause_acc = 5
            alki.head_y = alki.size / 1.8 + 252
            alki.body_y = 252
            alki.hair_y = 252

            background.acc = 5
            background.y = HEIGHT / 2 + 252

            pause.acc = 5
            pause.y = 102

            game_framework.mode = 'play'


def handle_events():
    global mouse_input, alki, background, pause, logo

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.stop_run()

        if game_framework.start_enable:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:  # 일시정지 메뉴
                    if mouse_input.input:
                        pause_resume_esc()
                    else:
                        game_framework.stop_run()

                if event.key == SDLK_SPACE:  # 스페이스바로 게임 시작
                    if not mouse_input.input:
                        logo.fadeout = True
                        logo.play_start_sound = True
                        logo.press_out = False

                        alki.start = True

            if event.type == SDL_MOUSEMOTION:  # 게임 마우스 입력, 게임 시작 이후부터 사용 가능
                if mouse_input.input and not (alki.pat and mouse_input.click):
                    mouse_input.mx, mouse_input.my = event.x, HEIGHT - 1 - event.y

            if event.type == SDL_MOUSEBUTTONDOWN:
                if event.button == SDL_BUTTON_LEFT:
                    if mouse_input.input:
                        mouse_input.click = True

            if event.type == SDL_MOUSEBUTTONUP:
                if event.button == SDL_BUTTON_LEFT:
                    if mouse_input.input:
                        mouse_input.click = False


def init():
    global mouse_input, alki, background, pause, logo

    mouse_input = MouseInput()  # 마우스 입력
    effect = Effect(mouse_input)

    background = Background(effect)  # 배경
    logo = Logo()
    alki = Alki(mouse_input, effect)  # 알키
    pause = Pause(mouse_input)

    start_logo = StartLogo()

    game_manager.add_object(mouse_input, 0)
    game_manager.add_object(effect, 0)
    game_manager.add_object(background, 0)
    game_manager.add_object(alki, 1)
    game_manager.add_object(pause, 6)
    game_manager.add_object(logo, 7)
    game_manager.add_object(start_logo, 7)


def update():
    game_manager.update()


def draw():
    clear_canvas()
    game_manager.render()
    update_canvas()


def finish():
    pass


def pause():
    pass


def resume():
    pass
