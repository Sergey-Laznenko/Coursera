"""
Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES
(в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
"""

numbers = [int(i) for i in input().split()]
before = set()
for num in numbers:
    if num in before:
        print('YES')
    else:
        print('NO')
        before.add(num)
