a, b, c = int(input()), int(input()), int(input())
count = 2
time_stop1, time_stop2 = 0, 0
d, e = 0, 0
j = 0
locMaxCount = 0
while a != 0 and b != 0 and c != 0:
    count += 1
    if a < b and c < b:
        locMaxCount += 1
        time_stop2 = time_stop1
        time_stop1 = count - 1
        if locMaxCount > 1:
            d = time_stop1 - time_stop2
            if e == 0:
                e = d
                d = 0
            else:
                if e > d:
                    e = d
                    d = 0
    (a, b) = (b, c)
    c = int(input())
print(e)
