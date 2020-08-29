"""
Даны действительные коэффициенты a, b, c, при этом a != 0.
Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.
"""

from math import sqrt

a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - 4 * a * c

if D > 0 and a > 0:
    x1 = (- b - sqrt(D)) / (2 * a)
    x2 = (- b + sqrt(D)) / (2 * a)
    print(round(x1, 6), round(x2, 6))
elif D > 0 > a:
    x1 = (- b - sqrt(D)) / (2 * a)
    x2 = (- b + sqrt(D)) / (2 * a)
    print(round(x2, 6), round(x1, 6))
elif D == 0:
    x = - b / (2 * a)
    print(x)
