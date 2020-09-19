"""
Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его,
отсортировав по фамилии в лексикографическом порядке. При выводе указываете фамилию, имя участника и его балл.

Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8. Например,
для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8').
"""


infile = open('input.txt', 'r', encoding='utf-8')
outfile = open('output.txt', 'w', encoding='utf-8')
data = []
for line in infile:
    surname, name, school, score = line.split()
    data.append([surname, name, score])
data.sort()
for line in data:
    a = ' '.join(line)
    print(a, file=outfile)
outfile.close()
