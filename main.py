from pico2d import *

from game_work import game_framework
from game_mods import play_mode as start_mode
from config import *

open_canvas(WIDTH, HEIGHT, False, True)

game_framework.run(start_mode)

close_canvas()
