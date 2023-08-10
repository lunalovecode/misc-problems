import math
n = int(input())
next_multiple = (math.ceil(n / 100) * 100) if n % 100 != 0 else ((n // 100) + 1) * 100
print(next_multiple - n)