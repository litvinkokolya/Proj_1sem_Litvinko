from math import sqrt
a, b, c = 7, 2, 8

def triangle_perimeter(a = a, b = b, c = c):
    return a + b + c

def triangle_area(a = a, b = b, c = c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))
