t = int(input())
for _ in range(t):
    carpet = []
    global n, m
    n, m = [int(x) for x in input().split()]
    for _ in range(n):
        carpet.append(input())
    cols = ["".join([carpet[r][c] for r in range(n)]) for c in range(m)]
    col_nums = [-1, -1, -1, -1]
    seen = [False, False, False, False]
    i = 0
    for col in cols:
        if "v" in col and seen[0] == False:
            col_nums[0] = i
            seen[0] = True
        elif "i" in col and seen[1] == False and seen[0] == True:
            col_nums[1] = i
            seen[1] = True
        elif "k" in col and seen[2] == False and all(x == True for x in seen[:2]):
            col_nums[2] = i
            seen[2] = True
        elif "a" in col and seen[3] == False and all(x == True for x in seen[:3]):
            col_nums[3] = i
            seen[3] = True
        i += 1

    
    c2 = [*col_nums]
    c2.sort()
    print("YES" if -1 not in col_nums and col_nums == c2 else "NO")
