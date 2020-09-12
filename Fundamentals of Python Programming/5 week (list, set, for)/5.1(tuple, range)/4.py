"""
По данному натуральном n вычислите сумму 1²+2²+3²+...+n².
"""

num = int(input())
res = 0
for i in range(1, num + 1):
    m = i ** 2
    res += m
print(res)
