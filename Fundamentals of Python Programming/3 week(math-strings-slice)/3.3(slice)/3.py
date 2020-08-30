"""
Дана строка, в которой буква h встречается минимум два раза.Удалите из этой строки первое и
последнее вхождение буквы h,а также все символы, находящиеся между ними.
"""

string = input()
first = string.find('h')
revers = string[::-1]
last = len(string) - revers.find('h')

print(string[:first] + string[last:])
