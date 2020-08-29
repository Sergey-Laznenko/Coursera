"""
Дана последовательность натуральных чисел x₁, x₂ ..., xn.
Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""

from math import sqrt
n, x = -1, -1
sum_x_step, sum_x = 0, 0
while x != 0:
    x = float(input())
    sum_x += x
    sum_x_step += x**2
    n += 1
s = sum_x / n
print(sqrt((sum_x_step - (n*s**2)) / (n - 1)))
