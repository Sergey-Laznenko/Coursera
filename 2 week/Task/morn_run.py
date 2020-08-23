x, y = int(input()), int(input())
score = 1
while x < y:
    x *= 1.1
    score += 1
print(score)
