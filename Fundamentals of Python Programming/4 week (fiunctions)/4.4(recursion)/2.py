"""
Дано действительное положительное число a и целое число n. Вычислите aⁿ. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степерь пользоваться нельзя.
"""


def power(x, y):
    b = 1
    result = x
    if y == 0:
        return 1
    if y > 0:
        while b < y:
            result = result * x
            b += 1
        return result
    else:
        while b > y:
            result = result * 1 / x
            b -= 1
        return result


a = float(input())
n = int(input())
print(power(a, n))
