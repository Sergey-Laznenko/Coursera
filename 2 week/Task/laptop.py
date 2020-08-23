a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

r1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
r2 = (a1 // a2) * (c1 // b2) * (b1 // c2)
r3 = (b1 // a2) * (c1 // b2) * (a1 // c2)
r4 = (b1 // a2) * (a1 // b2) * (c1 // c2)
r5 = (c1 // a2) * (a1 // b2) * (b1 // c2)
r6 = (c1 // a2) * (b1 // b2) * (a1 // c2)

if r1 >= r2:
    r2 = r1
if r3 >= r4:
    d4 = r2
if r5 >= r6:
    r6 = r5

if r2 >= r4 and r2 >= r6:
    print(r2)
elif r4 >= r6:
    print(r4)
else:
    print(r6)
