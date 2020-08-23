num = int(input())
score = 0
while num != 0:
    if score <= num:
        score = num
    num = int(input())
print(score)
