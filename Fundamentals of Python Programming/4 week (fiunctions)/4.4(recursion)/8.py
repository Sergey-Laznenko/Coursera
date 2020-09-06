"""
По данным целым числам n и k (0≤k≤n) вычислите C из n по k.
Решение оформите в виде функции C(n, k).
"""


def fact(a):
    if a == 0:
        return 1
    return a * fact(a - 1)


def c(x, y):
    return int(fact(x) / (fact(x - y) * fact(y)))


n, k = int(input()), int(input())
print(c(n, k))
