"""
Найдите количество положительных элементов в данном списке.
"""


a = input().split()
j = 0
for i in range(len(a)):
    if int(a[i]) > 0:
        j += 1
print(j)
