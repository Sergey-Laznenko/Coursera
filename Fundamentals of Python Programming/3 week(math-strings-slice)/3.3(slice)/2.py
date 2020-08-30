"""
Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
Если она встречается два и более раз, выведите индекс её первого и последнего появления.
Если буква f в данной строке не встречается, ничего не выводите.
При решении этой задачи нельзя использовать метод count и циклы.
"""

string = input()
first = string.find('f')
revers = string[::-1]
second = len(string) - revers.find('f') - 1
if first == second:
    print(first)
elif first == -1 or second == -1:
    print()
else:
    print(first, second)
