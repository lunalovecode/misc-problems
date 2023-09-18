t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    b = list(set(a))
    b.sort()
    if a == b:
        print("YES")
    else:
        print("NO")