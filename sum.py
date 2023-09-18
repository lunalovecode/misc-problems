n = int(input())
for _ in range(n):
    a, b, c = [int(x) for x in input().split()]
    m = max([a, b, c])
    if a == m:
        print("YES" if b + c == a else "NO")
    elif b == m:
        print("YES" if a + c == b else "NO")
    else:
        print("YES" if a + b == c else "NO")