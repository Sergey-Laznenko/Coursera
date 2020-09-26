"""
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны. Для одного данного слова определите его синоним.
"""


n, words = int(input()), dict()
for k in range(n):
    c = input()
    index = c.find(' ')
    words[c[:index]], words[c[index + 1:]] = c[index + 1:], c[:index]
print(words[input()])
