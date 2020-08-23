a, b, c, = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

if (a <= d and a <= e) or (b <= d and b <= e) or (c <= d and c <= e):
    print("YES")
else:
    print("NO")
