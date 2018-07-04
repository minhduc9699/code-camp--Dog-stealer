from math import sqrt


def get_distance(vector1, vector2):
    x1, y1 = vector1
    x2, y2 = vector2

    return sqrt((x1 - x2)**2 + (y1 - y2)**2)
