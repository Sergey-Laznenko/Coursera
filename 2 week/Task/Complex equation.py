a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == 0 and b == 0:
    print('INF')
elif (c * (-b // a) + d) == 0 or a == 0 or b % a != 0:
    print('NO')
else:
    print(-b // a)
