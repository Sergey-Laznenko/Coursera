"""
Теорема Лагранжа утверждает, что любое натуральное число можно представить в виде суммы четырех точных квадратов.
По данному числу n найдите такое представление: напечатайте от 1 до 4 натуральных чисел,
квадраты которых дают в сумме данное число.
"""


def lagrange(x, level):
    if level == 0:
        return "NO"
    sqrtx = int(x ** 0.5)
    if sqrtx * sqrtx == x:
        return str(sqrtx)
    while sqrtx > 0:
        if lagrange(x - sqrtx * sqrtx, level - 1) != "NO":
            return str(sqrtx) + " " + lagrange(x - sqrtx * sqrtx, level - 1)
        sqrtx -= 1
    return "NO"


n = int(input())
print(lagrange(n, 4))
