def sort2(a, b):
    if a < b:
        return a, b
    return b, a


minimum, maximum = sort2(5, 4)
print(maximum, minimum)
