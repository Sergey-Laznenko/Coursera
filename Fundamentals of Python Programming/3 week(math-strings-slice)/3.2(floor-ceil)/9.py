"""
Даны произвольные действительные коэффициенты a, b, c. Решите уравнение ax²+bx+c=0.
"""

a, b, c = float(input()), float(input()), float(input())
d = b**2 - (4 * a * c)
if d < 0 or a == b == 0 and c != 0:
    print(0)
elif a == b == c == 0:
    print(3)
elif d == 0 and a != 0:
    x1 = -b / (2 * a)
    print(1, x1)
elif d > 0 and a != 0:
    x1 = (-b - d**0.5) / (2 * a)
    x2 = (-b + d**0.5) / (2 * a)
    if x1 < x2:
        print(2, x1, x2)
    else:
        print(2, x2, x1)
elif a == 0:
    print(1, -c / b)
