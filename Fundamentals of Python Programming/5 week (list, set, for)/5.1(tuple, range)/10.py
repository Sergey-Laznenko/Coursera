"""
По данному натуральному n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл.
"""

num = int(input())
k = 1
my_sum = 0
if num == 0 or num == 1:
    print(k)
elif num >= 2:
    for i in range(1, num + 1):
        k *= i
        my_sum += k
    print(my_sum)
