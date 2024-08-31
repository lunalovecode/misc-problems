t = int(input())
for _  in range(t):
    n, c = input().split()
    n = int(n)
    sequence = input()
    if c == "g":
        print(0)
        continue
    
    last_g = -1
    ans = 0
    s2 = sequence + sequence
    for i in range((n * 2) - 1, 0, -1):
        if s2[i] == "g":
            last_g = i
        elif s2[i] == c:
            ans = max(ans, last_g - i)
    
    print(ans)