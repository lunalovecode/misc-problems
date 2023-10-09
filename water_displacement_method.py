import math
X = int(input())
Y = int(input())
V  = Y - X
# V = (4 / 3) * pi * (r ** 3)
r = (3 * (V / (4 * math.pi))) ** (1 / 3)
print(r * 2)