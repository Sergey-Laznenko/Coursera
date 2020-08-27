n = int(input())

h = n // 3600 % 24
m = n // 60 % 60
s = n % 60

print(f'{h}:{m // 10}{m % 10}:{s // 10}{s % 10}')
