n = int(input())
left = n // 100
right = ((n % 10) * 10) + ((n // 10) % 10)
print((left - right + 1) ** 2)
