"""
В обувном магазине продается обувь разного размера. Известно, что одну пару обуви можно надеть на другую,
если она хотя бы на три размера больше. В магазин пришел покупатель.Требуется определить,
какое наибольшее количество пар обуви сможет предложить ему продавец так, чтобы он смог надеть их все одновременно.

Сначала вводится размер ноги покупателя (обувь меньшего размера он надеть не сможет),
в следующей строке — размеры каждой пары обуви в магазине через пробел. Размер — натуральное число,
не превосходящее 100.
"""


size = int(input())
a = list(map(int, input().split()))
a.sort()
score = 0
for i in a:
    if i >= size:
        score += 1
        size = i + 3
print(score)