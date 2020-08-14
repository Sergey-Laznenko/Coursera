a = int(input())
b = int(input())

c = 0 ** (b // (a + 1)) * a
d = 0 ** (a // b) * b
print(c + d)
