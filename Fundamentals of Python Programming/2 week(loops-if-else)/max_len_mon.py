now = int(input())
i1 = i2 = 1
max_len1 = 1
while now != 0:
    prev = now
    now = int(input())
    if now > prev:
        i1 += 1
        if max_len1 <= i1:
            max_len1 = i1
    elif now <= prev:
        i1 = 1
    if now < prev and now != 0:
        i2 += 1
        if max_len1 <= i2:
            max_len1 = i2
    elif now >= prev:
        i2 = 1
print(max_len1)
