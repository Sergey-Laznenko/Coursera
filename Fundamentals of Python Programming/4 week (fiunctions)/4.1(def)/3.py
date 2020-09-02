"""
Напишите функцию, вычисляющую длину отрезка по координатам его концов. С помощью этой функции напишите программу,
вычисляющую периметр треугольника по координатам трех его вершин.
"""

from math import sqrt


def distance(x1, y1, x2, y2, x3, y3):
    first = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    second = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    third = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    result = first + second + third
    return result


x1, y1, = int(input()), int(input())
x2, y2, = int(input()), int(input())
x3, y3 = int(input()), int(input())

print(distance(x1, y1, x2, y2, x3, y3))
