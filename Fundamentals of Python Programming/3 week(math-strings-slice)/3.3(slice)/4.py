"""
Дана строка, в которой буква h встречается как минимум два раза. Выведите измененную строку:
повторите последовательность символов, заключенную между первым и последним появлением буквы h два раза
(сами буквы h не входят в повторяемый фрагмент, т. е. их повторять не надо).
"""

string = input()
first = string.find('h')
last = string.rfind('h')
print(string[:last] + string[first + 1:last] + string[last:])
