"""
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def cnk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


print(cnk(4, 2))
"""