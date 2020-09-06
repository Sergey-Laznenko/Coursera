"""
Дана последовательность чисел, завершающаяся числом 0.
Найдите сумму всех этих чисел, не используя цикл.
"""


def my_sum(x):
    if x == 0:
        return x
    else:
        return x + my_sum(int(input()))


n = int(input())
print(my_sum(n))
