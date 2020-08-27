n = int(input())
x, z = 1, 1
while n >= z:
    print(z, end=' ')
    z = 2 ** x
    x += 1
