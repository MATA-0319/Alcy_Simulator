from game_class_manager.alki_manager import set_state, move_eye, head_animation, output, init_alki, start_animation, \
    update_blink, \
    update_pat, init_deg, load_alki_file, pause_resume_alki, update_result

from game_work import game_framework


class Alki:
    body = None

    def __init__(self, m, e):
        load_alki_file(Alki)
        init_alki(self, m, e)

    def draw(self):
        output(self, Alki)

    def update(self):
        start_animation(self)
        update_blink(self)
        pause_resume_alki(self)
        update_result(self)

        if self.m.input:
            set_state(self)
            head_animation(self)
            move_eye(self)

        if self.pat and self.m.click:
            if game_framework.mode == 'play':  # play 모드에서만 가능
                update_pat(self)
        else:
            init_deg(self)

