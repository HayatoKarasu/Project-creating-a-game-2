from random import randint

def randbool(r, mxr):
    t = randint(0, mxr)
    return (t <= r)

def randcell(w, h):
    tw = randint(0, w - 1)
    th = randint(0, h - 1)
    return (th, tw)

# 0 - наверх, 1 - направо, 2 - вниз, 3 - налево
def randcell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = randint(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)
