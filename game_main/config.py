from tkinter import *

# 현재 모니터 크기를 인식하여 자동으로 창 사이즈를 조정한다.
root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
print(WIDTH, HEIGHT)

# 게임 전체 속도
PIXEL_RATIO = 80
TS = (5 * PIXEL_RATIO)  # Time Sync, 게임에서 사용하는 시간 동기화 비율

# 알키 이미지 경로
alki_body = 'res//alki//body.png'
alki_head_middle = 'res//alki//head_middle.png'
alki_head_right = 'res//alki//head_right.png'
alki_head_left = 'res//alki//head_left.png'

alki_hair = 'res//alki//hair.png'
alki_tail = 'res//alki//tail.png'

alki_eye_middle = 'res//alki//face//eye_middle.png'
alki_dot_middle = 'res//alki//face//dot_middle.png'
alki_brow_middle = 'res//alki//face//brow_middle.png'

alki_eye_right = 'res//alki//face//eye_right.png'
alki_dot_right = 'res//alki//face//dot_right.png'
alki_brow_right = 'res//alki//face//brow_right.png'

alki_eye_left = 'res//alki//face//eye_left.png'
alki_dot_left = 'res//alki//face//dot_left.png'
alki_brow_left = 'res//alki//face//brow_left.png'

# 배경 경로
background_image = 'res//background.png'

# 커서 경로
cursor_image = 'res//cursor.png'
