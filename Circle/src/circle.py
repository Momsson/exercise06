import math

def radius_sum(r1, r2):
    return r1 + r2


def has_intersection(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distance <= r1 + r2