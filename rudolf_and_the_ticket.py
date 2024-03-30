t = int(input())
for _ in range(t):
    n, m, k = [int(x) for x in input().split()]
    left = [int(x) for x in input().split()]
    right = [int(x) for x in input().split()]
    ans = 0
    if all([x >= k for x in left]):
        print(0)
        continue
    if all([x >= k for x in right]):
        print(0)
        continue
    
    # count how many coins in the left pocket are < k
    # for l in each of those each of those coins, count how many coins there are in right such that l + r <= k
    less_than_k = [x for x in left if x < k]
    for l in less_than_k:
        for r in right:
            if l + r <= k:
                ans += 1
            else:
                continue

    print(ans)