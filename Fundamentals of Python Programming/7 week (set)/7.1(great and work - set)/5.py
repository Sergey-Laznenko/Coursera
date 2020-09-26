n, m = map(int, input().split())
a = set([input() for _ in range(n)])
b = set([input() for _ in range(m)])
c = a & b
for x in [c, a - c, b - c]:
    print(len(x))
    print(*(sorted(map(int, x))))
