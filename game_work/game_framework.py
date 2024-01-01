import time

from config import TS

running = None
stack = None
start_enable = False
mode = 'play'


# DEBUG = False


def change_mode(mode):
    global stack
    if len(stack) > 0:
        stack[-1].finish()
        stack.pop()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    global stack
    if len(stack) > 0:
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    global stack
    if len(stack) > 0:
        stack[-1].finish()
        stack.pop()

    if len(stack) > 0:
        stack[-1].resume()


def stop_run():
    global running
    running = False


def run(start_mode):
    global running, stack, frame_time, ts
    running = True
    stack = [start_mode]
    start_mode.init()

    ts, frame_time = 0, 0.0
    current_time = time.time()

    while running:
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
        frame_time = time.time() - current_time
        current_time += frame_time
        ts = TS * frame_time  # 게임 시간 동기화 값, 모든 움직이는 동작에 곱해야 함.

    while len(stack) > 0:
        stack[-1].finish()
        stack.pop()
