import math
# n = int(input())
# n = 10
# 525631075

# n = 13 ** 7
# 19524775

# n = 10 ** 18
# 454770529

n = 7 ** (7 ** (7 ** 2023))

x = 0

def power(a, n, m):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a % m, n // 2, m)
    else:
        return a * power(a * a % m, (n - 1) // 2,m) % m
        

if n % 2 == 0:
    x = 2 * power(105, n / 2, 1000000007)
else:
    x = 26 * power(105, (n - 1) / 2, 1000000007)

print(x % 1000000007)