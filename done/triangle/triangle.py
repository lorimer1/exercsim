def is_triangle(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return a + b >= c and a + c >= b and b + c >= a and not 0 in sides


def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) < 3


def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3
