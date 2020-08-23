num = int(input())
score = 0
while num != 0:
    num2 = int(input())
    if num2 > num:
        score += 1
    num = num2
print(score)
