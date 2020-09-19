"""
В олимпиаде по информатике принимало участие несколько человек.

Определите и выведите средние баллы участников олимпиады в 9 классе, в 10 классе, в 11 классе.

"""


klas = dict()
with open('input.txt', encoding='utf-8') as file:
    for line in file:
        s = line.strip().split()
        klas[int(s[-2])] = klas.get(int(s[-2]), []) + [int(s[-1])]
print(*[sum(klas[key]) / len(klas[key]) for key in sorted(klas.keys())])
