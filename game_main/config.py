from tkinter import *

# 현재 모니터 크기를 인식하여 자동으로 창 사이즈를 조정한다.
root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
print(WIDTH, HEIGHT)

# 게임 전체 속도
PIXEL_RATIO = 150
TS = (5 * PIXEL_RATIO)  # Time Sync, 게임에서 사용하는 시간 동기화 비율


# 알키 이미지 경로
alki_head_middle = 'res//alki//head_middle.png'
alki_head_right = 'res//alki//head_right.png'
alki_head_left = 'res//alki//head_left.png'
alki_body = 'res//alki//body.png'
