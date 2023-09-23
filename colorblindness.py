t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    ans = "YES"
    for x in range(n):
        if not (a[x] == b[x] or (a[x] == "G" and b[x] == "B") or (a[x] == "B" and b[x] == "G")):
            ans = "NO"
            break
    print(ans)