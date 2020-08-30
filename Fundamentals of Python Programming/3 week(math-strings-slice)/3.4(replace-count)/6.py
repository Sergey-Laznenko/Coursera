text = input()
for i in range(len(text)):
    if i % 3 != 0:
        print(text[i], end="")
