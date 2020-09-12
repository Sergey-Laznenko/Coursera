"""
Выведите все четные элементы списка.
"""


print(*[num for num in input().split() if not int(num) % 2])
