n = int(input())
sum_sq = 0
score = 0
while n != 0:
    sum_sq += n
    score += 1
    n = int(input())
print(sum_sq / score)
