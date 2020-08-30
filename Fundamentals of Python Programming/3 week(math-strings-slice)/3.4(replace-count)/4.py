"""
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
"""

text = input()
first = text.find('h')
last = text.rfind('h')
string = text[first + 1:last]
H = string.replace('h', 'H')
print(text[:first + 1] + H + text[last:])
