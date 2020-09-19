l1, r1, l2 = int(input()), int(input()), int(input())
r2, l3, r3 = int(input()), int(input()), int(input())
n1 = 1
n2 = 2
n3 = 3
if l2 < l1:
    (l1, l2) = (l2, l1)
    (r1, r2) = (r2, r1)
    (n1, n2) = (n2, n1)
if l3 < l2:
    (l2, l3) = (l3, l2)
    (r2, r3) = (r3, r2)
    (n2, n3) = (n3, n2)
if l2 < l1:
    (l1, l2) = (l2, l1)
    (r1, r2) = (r2, r1)
    (n1, n2) = (n2, n1)
d1 = r1 - l1
d2 = r2 - l2
d3 = r3 - l3
c1 = l2 - r1
c2 = l3 - r2
if (l2 <= r1 and l3 <= r2) or r1 >= l3:
    print(0)
elif d1 < c2 and d3 < c1:
    print(-1)
elif (n1 < n3 and d1 >= c2 > 0) or (n1 < n3 and c2 <= 0 and c1 > 0):
    print(n1)
elif d3 >= c1 > 0:
    print(n3)
elif (n3 < n1 and d3 >= c1 > 0) or (n3 < n1 and c1 <= 0 and c2 > 0):
    print(n3)
elif (d1 >= c2 > 0) or (c2 <= 0 and d1 >= c1 > 0):
    print(n1)
