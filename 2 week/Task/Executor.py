a, b = int(input()), int(input())
while a > b:
    if a % 2 == 0 and a // 2 >= b:
        a //= 2
        print(':2')
    else:
        a -= 1
        print('-1')
