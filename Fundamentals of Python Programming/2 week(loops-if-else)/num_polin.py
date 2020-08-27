n = int(input())
i = 1
counter = 0
while i <= n:
    int_to_str = str(i)
    reverse_num = (int_to_str[::-1])
    if i == int(reverse_num):
        counter += 1
    i += 1
print(counter)
