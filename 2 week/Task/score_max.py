n = int(input())
max_num = n
score = 1

while n != 0:
    if n > max_num:
        max_num = n
        score = 1
    n = int(input())
    if n == max_num:
        score += 1
print(score)
