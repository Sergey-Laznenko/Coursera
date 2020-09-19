"""
Даны числа a, b, c, d, e. Подсчитайте количество таких целых чисел от 0 до 1000 (включительно),
которые являются корнями уравнения (ax³+bx²+cx+d)/(x-e)=0, и выведите их количество.
"""

a, b, c, d, e = [int(input()) for _ in range(5)]
count = 0
for x in range(0, 1001):
    if x - e and not (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e):
        count += 1
print(count)
