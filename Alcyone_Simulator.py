from pico2d import *

from config import *
from game_mods import play_mode as start_mode
from game_work import game_framework

open_canvas(WIDTH, HEIGHT, False, False)
hide_lattice()
hide_cursor()
game_framework.run(start_mode)

close_canvas()
