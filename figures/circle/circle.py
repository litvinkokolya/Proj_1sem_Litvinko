from math import pi

default_perimeter = 5
def circle_perimeter(d = default_perimeter):
    return pi * d

def circle_area(d = default_perimeter):
    return pi * pow(d, 2)