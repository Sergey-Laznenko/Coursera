import sys

input_data = sys.stdin.readlines()
list_prez = dict()
win_prez = list()
for l in input_data:
    list_prez[l] = list_prez.get(l, 0) + 1
for l in list_prez:
    win_prez.append((list_prez[l], l))
win_prez = sorted(win_prez)
if win_prez[-1][0] > len(input_data) / 2:
    print(win_prez[-1][1])
else:
    print(win_prez[-1][1], win_prez[-2][1], sep="")
