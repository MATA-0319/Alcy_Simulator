# 게임 월드의 표현
game = [[], [], [], [], [], [], [], []]
collision_pairs = {}


def add_object(o, depth=0):
    game[depth].append(o)  # 지정된 깊이의 레이어에 객체 추가


def update():
    for layer in game:
        for o in layer:
            o.update()


def render():
    for layer in game:
        for o in layer:
            o.draw()


def add_collision_pair(group, a, b):  # add_collision_pair('boy:ball', None, ball)
    if group not in collision_pairs:  # 딕셔너리에 그룹이 없다면
        collision_pairs[group] = [[], []]

    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def handle_collisions():
    collided_pairs = []
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    collided_pairs.append((group, a, b))
    for group, a, b in collided_pairs:
        a.handle_collision(group, b)
        b.handle_collision(group, a)


def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def remove_object(o):
    for layer in game:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Cannot delete non existing object')


def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb:
        return False
    if ra < lb:
        return False
    if ta < bb:
        return False
    if ba > tb:
        return False

    return True


def clear():
    for layer in game:
        for o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
        layer.clear()
