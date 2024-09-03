t = int(input())
for _ in range(t):
    l, r, x = [int(x) for x in input().split()]
    start, target = [int(x) for x in input().split()]
    if start == target:
        print(0)
    elif abs(start - target) >= x:
        print(1)
    elif r - max(start, target) >= x or min(start, target) - l >= x:
        print(2)
    elif (r - target >= x and start - l >= x) or (r - start >= x and target - l >= x):
        print(3)
    else:
        print(-1)