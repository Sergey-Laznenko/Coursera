"""
Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел, которая не содержит инструкции if,
а использует стандартную функцию min от двух чисел. Считайте четыре целых числа и выведите их минимум.
"""

def min_num(a, b, c, d):
    x = min(a, b, c, d)
    return x


a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min_num(a, b, c, d))
