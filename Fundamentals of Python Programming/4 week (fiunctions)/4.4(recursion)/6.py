"""
Даны два натуральных числа n и m.

Сократите дробь (n / m), то есть выведите два других числа p и q таких,
что (n / m) = (p / q) и дробь (p / q) — несократимая.

Решение оформите в виде функции ReduceFraction(n, m), получающая значения n и m
и возвращающей кортеж из двух чисел: return p, q
"""


def func(x, y):
    if y == 0:
        return x
    return func(y, x % y)


n, m = int(input()), int(input())


def reduce_fraction(x, y):
    return x // func(x, y), y // func(x, y)


print(*reduce_fraction(n, m))
