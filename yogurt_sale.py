t = int(input())
for _ in range(t):
    n, a, b = [int(x) for x in input().split()]
    cost = 0
    if b / 2 < a:
        if n % 2 == 0:
            cost = int((n / 2) * b)
        else:
            cost = int(((n - 1) / 2) * b) + a
    else:
        cost = n * a
    print(cost)
