from random import uniform
from math import pow
import threading


def random_point():
    return uniform(-1, 1), uniform(-1, 1)

def hit_or_miss(xy):
    if pow(xy[0], 2) + pow(xy[1], 2) < 1:
        return True # its inside the circle
    else:
        return False # outside


# area or circle = 2pir² area of square = 4r² so area_circle/area_square = pi/4,
# therefore te numbers of points inside circle/total_point =  aprox pi/4
def pi():
    inside_circle = 0
    iterations = 10000000
    for i in range(iterations):
        if hit_or_miss(random_point()):
            inside_circle += 1
    result = inside_circle/iterations
    result = result*4
    return result


print(pi())



