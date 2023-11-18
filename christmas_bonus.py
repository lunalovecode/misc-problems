def gcd(a, b, x, y):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = gcd(b, a % b, x, y)
    x, y = y1, x1 - y1 * (a // b)
    return d, x, y

def mod_inverse(a, m, x, y):
    d, x, y = gcd(a, m, x, y)
    return x % m

a = int(input())
b = int(input())
x = int(input())
y = int(input())

print("IMPOSSIBLE" if mod_inverse(b, a, x, y) == 0 else mod_inverse(b, a, x, y))