n = int(input())
c = list(map(int, input().split()))
k = int(input())
pj = list(map(int, input().split()))
a = [0] * (max(pj))
for i in range(len(pj)):
    a[pj[i] - 1] += 1
for i in range(len(a)):
    if a[i] > c[i]:
        print('YES')
    else:
        print('NO')
