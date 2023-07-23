t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    ct = 0
    longest = -1000000000000
    for x in a:
        if x == "0":
            ct += 1
        else:
            ct = 0
        longest = max(longest, ct)
    print(longest)