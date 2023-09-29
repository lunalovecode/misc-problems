t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    if a.count(k) == 0:
        print("NO")
    else:
        print("YES")