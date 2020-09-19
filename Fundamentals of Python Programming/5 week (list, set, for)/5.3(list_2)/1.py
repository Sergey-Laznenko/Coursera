"""
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы,
стоящие правее элемента с индексом k.

Программа получает на вход список, затем число k. Программа сдвигает все элементы,
а после этого удаляет последний элемент списка при помощи метода pop().

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
Также нельзя использовать дополнительный список.
"""


list1 = input().split()
k = int(input())
for i in range(k, len(list1) - 1):
    list1[i] = list1[i + 1]
list1.pop()
print(' '.join(list1))