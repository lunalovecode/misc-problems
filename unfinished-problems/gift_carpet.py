def is_subsequence(subsequence, string):
    n, m, i, j = len(subsequence), len(string), 0, 0
    while i < n and j < m:
        if subsequence[i] == string[j]:
            i += 1
        j += 1
    
    return i == n

t = int(input())
for _ in range(t):
    carpet = []
    global n, m
    n, m = [int(x) for x in input().split()]
    for _ in range(n):
        carpet.append(input())
    cols = ["".join([carpet[r][c] for r in range(n)]) for c in range(m)]
    in_rows = False
    ans = "NO"
    for row in carpet:
        if is_subsequence("vika", row):
            in_rows = True
    if in_rows:
        ans = "YES"
    else:
        for col in cols:
            if is_subsequence("vika", col):
                ans = "YES"

    print(ans)
