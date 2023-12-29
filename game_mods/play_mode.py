from pico2d import *

from game_work import game_manager, game_framework
from game_main.config import *


def handle_events():
    global image, image2, image3
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.stop_run()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.stop_run()


def init():
    pass


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
