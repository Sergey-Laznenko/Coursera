"""
В списке все элементы попарно различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""


mas = [int(i) for i in input().split()]
max_el = mas.index(max(mas))
min_el = mas.index(min(mas))
if len(mas) > 0:
    mas[max_el], mas[min_el] = mas[min_el], mas[max_el]
print(' '.join([str(i) for i in mas]))
