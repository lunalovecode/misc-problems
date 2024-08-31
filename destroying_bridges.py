t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    bridges = (n * (n - 1)) // 2
    visitable = n
    if k >= n - 1:
        visitable = 1
    print(visitable)