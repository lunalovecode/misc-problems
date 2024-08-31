t = int(input())
for _ in range(t):
    n = int(input())
    directions = input()
    ans = 0
    if ">" not in directions or "<" not in directions:
        ans = n
    else:
        directions += directions[0]
        for i in range(n):
            if directions[i] == "-" or directions[i + 1] == "-":
                ans += 1
    print(ans)