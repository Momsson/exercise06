import math


def radius_sum(r1, r2):
    return r1 + r2


def euclid_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def has_intersection(circle_1, circle_2):

    x1, y1, r1 = circle_1["x"], circle_1["y"], circle_1["r"]
    x2, y2, r2 = circle_2["x"], circle_2["y"], circle_2["r"]

    d = euclid_distance(x1, y1, x2, y2)

    sum_r = r1 + r2
    diff_r = abs(r1 - r2)

    if math.isclose(d, sum_r) or math.isclose(d, diff_r):
        return {"is_intersection": True, "intersections_count": 1}

    elif diff_r < d < sum_r:
        return {"is_intersection": True, "intersections_count": 2}

    else:
        return {"is_intersection": False, "intersections_count": 0}