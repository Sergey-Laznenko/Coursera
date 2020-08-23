num = int(input())
score = 0
delta = num
total = 0
while num != 0:
    if num == delta:
        score += 1
        if score > total:
            total = score
    else:
        delta = num
        score = 1
    num = int(input())
print(total)
