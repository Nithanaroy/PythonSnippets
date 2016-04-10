import math


class fPoint():
    def __init__(self):
        self.x = 0
        self.y = 0


def sign(p1, p2, p3):
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);


def PointInTriangle(pt, v1, v2, v3):
    b1 = sign(pt, v1, v2) < 0.0;
    b2 = sign(pt, v2, v3) < 0.0;
    b3 = sign(pt, v3, v1) < 0.0;

    return ((b1 == b2) and (b2 == b3));


def pointsBelongToTriangle(x1, y1, x2, y2, x3, y3, p1, q1, p2, q2):
    ab = distance(x1, y1, x2, y2)
    bc = distance(x2, y2, x3, y3)
    ac = distance(x1, y1, x3, y3)
    if ab + bc > ac and ab + ac > bc and bc + ac > ab:
        return 0


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
