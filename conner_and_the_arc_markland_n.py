# i hate off by one bugs
t = int(input())
for _ in range(t):
    n, c, k = [int(x) for x in input().split()]
    closed = [int(x) for x in input().split()]
    ans = k

    for i in range(c, n + 1):
        if i not in closed:
            ans = min(ans, abs(i - c))
            break
    
    for i in range(c, 0, -1):
        if i not in closed:
            ans = min(ans, abs(i - c))
            break
    
    print(ans)
