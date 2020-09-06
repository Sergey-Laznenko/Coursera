"""
Дано натуральное число n>1. Проверьте, является ли оно простым. Программа должна вывести слово YES,
если число простое и NO, если число составное.
"""


def is_prime(x):
    i = 2
    prime = False
    while i <= x ** 0.5:
        if x % i == 0:
            return prime
        i += 1
    return not prime


n = int(input())
if n == 2 or is_prime(n):
    print('YES')
else:
    print('NO')
