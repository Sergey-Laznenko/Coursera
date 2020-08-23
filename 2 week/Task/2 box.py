a1, b1, c1, = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

total_1 = a1 * b1 * c1
total_2 = a2 * b2 * c2
message = "Boxes are incomparable"

if b1 > c1:
    (b1, c1) = (c1, b1)
if a1 > c1:
    (a1, c1) = (c1, a1)
if a1 > b1:
    (a1, b1) = (b1, a1)

if b2 > c2:
    (b2, c2) = (c2, b2)
if a2 > c2:
    (a2, c2) = (c2, a2)
if a2 > b2:
    (a2, b2) = (b2, a2)

if total_1 == total_2 and a1 == a2 and b1 == b2 and c1 == c2:
    message = "Boxes are equal"
elif total_1 < total_2 and a1 <= a2 and b1 <= b2 and c1 <= c2:
    message = "The first box is smaller than the second one"
elif total_1 > total_2 and a1 >= a2 and b1 >= b2 and c1 >= c2:
    message = "The first box is larger than the second one"

print(message)
