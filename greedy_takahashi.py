a, b, k = [int(x) for x in input().split()]
if a >= k:
    print(a - k, b)
else:
    print(0, max(a + b - k, 0))