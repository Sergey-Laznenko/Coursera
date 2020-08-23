n = int(input())
score = 0

while n != 0:
    if n % 2 == 0:
        score += 1
    n = int(input())
print(score)
