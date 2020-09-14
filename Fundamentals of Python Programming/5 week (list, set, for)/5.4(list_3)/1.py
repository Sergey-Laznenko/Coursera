"""
Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.

"""


num = int(input())
my_list = list(map(int, input().split()))
x = int(input())
number = 1001
difference = 10000
for i in range(len(my_list)):
    if abs(my_list[i] - x) < difference:
        number = my_list[i]
        difference = abs(my_list[i] - x)
print(number)
