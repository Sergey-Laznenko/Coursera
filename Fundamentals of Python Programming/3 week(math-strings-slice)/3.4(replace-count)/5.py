"""
Дана строка. Получите новую строку, вставив между каждыми двумя символами исходной строки символ *.
Выведите полученную строку.
"""

text = input()
print(text.replace('', '*')[1:-1])
