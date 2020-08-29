"""
Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада через год.
Вклад составляет X рублей Y копеек. Определите размер вклада через K лет.
"""

rate = int(input())
rub, kop = int(input()), int(input())
year = int(input())
coins = rub * 100
totalCoins = coins + kop
score = 0
while score < year:
    score += 1
    totalCoins = totalCoins + int((rate / 100 * totalCoins))
print(int(totalCoins / 100), int(totalCoins % 100))
