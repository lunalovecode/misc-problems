t = int(input())
for _ in range(t):
    n = int(input())
    directions = input()
    x, y = 0, 0
    ans = "NO"
    for d in directions:
        if d == "U":
            y += 1
        elif d == "D":
            y -= 1
        elif d == "R":
            x += 1
        elif d == "L":
            x -= 1
        if x == y == 1:
            ans = "YES"
            break
    print(ans)