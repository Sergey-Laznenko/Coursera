p, x, y = int(input()), int(input()), int(input())
xy = float(x * 100 + y)
rate_xy = ((xy / 100 * p) + xy)
rub = int(rate_xy) // 100
cop = int(rate_xy) % 100
print(rub, cop, end=' ')
