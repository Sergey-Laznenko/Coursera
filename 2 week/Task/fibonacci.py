n = int(input())
a, b = 0, 1
if n == 0:
    b = a
while n > 1:
    a, b = b, (a + b)
    n -= 1
print(b)
