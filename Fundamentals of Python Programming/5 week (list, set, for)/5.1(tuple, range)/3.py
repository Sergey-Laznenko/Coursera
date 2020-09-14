"""
Дано натуральное число n. Напечатайте все n-значные нечетные натуральные числа в порядке убывания.
"""

n = int(input())
max_res = 10 ** n - 1
min_res = 10 ** (n - 1)
for i in range(max_res, min_res - 1, -2):
    print(i, end=' ')
