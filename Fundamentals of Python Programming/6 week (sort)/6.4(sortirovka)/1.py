"""
Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения от 0 до 100 (100 включая).

Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.

Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.
Использовать встроенные функции сортировки нельзя.
"""


myList = list(map(int, input().split()))


def CountSort(list_i):
    list_ii = [0] * (max(list_i) + 1)
    for now in list_i:
        list_ii[now] += 1
    b = 0
    for i in range(max(list_i) + 1):
        for j in range(list_ii[i]):
            list_i[b] = i
            b += 1
    return list_i


print(*CountSort(myList))
