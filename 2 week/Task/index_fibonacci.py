num = int(input())
a = 0
b = 1
counter = 1
while b < num:
    if num == 1:
        print(b)
    a, b = b, (a + b)
    counter += 1
if b == num and num != 0:
    print(counter)
elif num == 0:
    print(0)
else:
    print(-1)
