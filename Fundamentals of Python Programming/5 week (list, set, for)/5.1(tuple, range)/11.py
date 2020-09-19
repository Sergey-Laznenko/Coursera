"""
Для настольной игры используются карточки с номерами от 1 до N.Одна карточка потерялась.
Найдите ее, зная номера оставшихся карточек.
"""

num = int(input())
sum_total = 0
sum_input = 0
for j in range(num - 1):
    sum_input += int(input())
for i in range(num + 1):
    sum_total += i
number = sum_total - sum_input
print(number)
