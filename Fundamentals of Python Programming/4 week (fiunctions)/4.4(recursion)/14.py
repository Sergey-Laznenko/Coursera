"""
Напишите программу, которая представляет переданное натуральное число в виде суммы не более чем 7 кубов
других натуральных чисел.
"""


from math import *


def solve(n, a, t):
    c = n
    d = t
    while c > 0:
        if d > 0:
            x = trunc(float('{0:.11f}'.format((c ** (1 / 3))))) - 1
            d -= 1
        else:
            x = trunc(float('{0:.11f}'.format((c ** (1 / 3)))))
        if x <= 1:
            x = trunc(float('{0:.11f}'.format((c ** (1 / 3)))))
        if d > x:
            print(0)
            exit(0)
        a.append(x ** 3)
        c -= x ** 3
        if len(a) > 7:
            a.clear()
            solve(n, a, t + 1)
    print(*a)
    exit(0)


a = []
n = int(input())
t = 0
solve(n, a, t)
