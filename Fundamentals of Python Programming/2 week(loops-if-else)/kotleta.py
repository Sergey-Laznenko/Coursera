k, m, n = int(input()), int(input()), int(input())

if n <= k:
    print(m * 2)

elif n > k and n % k == 0:
    print(n // k * (m * 2))

elif n > k and n % k != 0 and n % k <= k * 0.5:
    print((n // k * (m * 2)) + m)

elif n > k and n % k != 0 and n % k > k * 0.5:
    print((n // k * (m * 2)) + m * 2)
