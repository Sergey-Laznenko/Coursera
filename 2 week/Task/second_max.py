n = int(input())
max_num = n
second_num = 0

while n != 0:
    n = int(input())
    if n > max_num:
        second_num = max_num
        max_num = n
    elif n != 0 and second_num < n:
        second_num = n
print(second_num)
