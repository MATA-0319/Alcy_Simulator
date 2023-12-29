from pico2d import *
from game_work import game_manager, game_framework


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():
    pass


def update():
    pass


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
