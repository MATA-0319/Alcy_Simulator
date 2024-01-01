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
alki_body = 'res//alcy//body.png'
alki_head_middle = 'res//alcy//head_middle.png'
alki_head_right = 'res//alcy//head_right.png'
alki_head_left = 'res//alcy//head_left.png'

alki_hair = 'res//alcy//hair.png'
alki_tail = 'res//alcy//tail.png'

alki_eye_middle = 'res//alcy//face//eye_middle.png'
alki_dot_middle = 'res//alcy//face//dot_middle.png'
alki_brow_middle = 'res//alcy//face//brow_middle.png'

alki_eye_right = 'res//alcy//face//eye_right.png'
alki_dot_right = 'res//alcy//face//dot_right.png'
alki_brow_right = 'res//alcy//face//brow_right.png'

alki_eye_left = 'res//alcy//face//eye_left.png'
alki_dot_left = 'res//alcy//face//dot_left.png'
alki_brow_left = 'res//alcy//face//brow_left.png'

alki_blink_middle = 'res//alcy//face//blink_middle.png'
alki_blink_right = 'res//alcy//face//blink_right.png'
alki_blink_left = 'res//alcy//face//blink_left.png'

# 배경 경로
background_image = 'res//background.png'

# 커서 경로
cursor_image = 'res//cursor.png'
cursor_hand_image = 'res//cursor_hand.png'

# ui 경로
pause_back = 'res//pause_background.png'
pause_button_image = 'res//pause_button.png'
menu_button_image = 'res//menu_button.png'
icon_pause_image = 'res//icon_pause.png'
icon_exit_image = 'res//icon_exit.png'
icon_info_image = 'res//icon_info.png'

# 폰트 경로
font = 'res//font//AppleSDGothic.ttf'

# 사운드 경로
button_click_sound = 'res//sound//button_click.ogg'
pat_sound_file = 'res//sound//pat.ogg'
