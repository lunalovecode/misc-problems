t = int(input())
for _ in range(t):
    n = int(input())
    seq = [int(x) for x in input().split()]
    ans = seq[0]
    for i in range(1, n):
        if i % 2 != 0:
            ans -= seq[i]
        else:
            ans += seq[i]
    print(ans)