"""
Дано несколько чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.
"""

num = int(input())
score = 0
for _ in range(num):
    a = int(input())
    if a == 0:
        score += 1
print(score)
