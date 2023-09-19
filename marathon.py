t = int(input())
for _ in range(t):
    a, b, c, d = [int(x) for x in input().split()]
    ct = [1 for x in [b, c, d] if x > a]
    print(sum(ct))