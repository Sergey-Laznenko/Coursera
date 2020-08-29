"""
Дано положительное действительное число X. Выведите его дробную часть.
"""
from math import floor

x = float(input())
result = x - floor(x)
print(round(result, 10))
