from tkinter import *

# 현재 모니터 크기를 인식하여 자동으로 창 사이즈를 조정한다.
root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

# 픽셀 비율
PIXEL_RATIO = 150  # 1미터 = 150픽셀

# 게임 전체 속도
TS = (5 * PIXEL_RATIO)  # Time Sync, 게임에서 사용하는 시간 동기화 비율
