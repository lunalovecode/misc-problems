from itertools import permutations

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    neighbors = [[] for _ in range(n)]
    nums = [_ for _ in range(1, len(a) + 1)]
    p = permutations(nums, 2)
    for u, v in p:
        if a[u - 1] - a[v - 1] >= b[u - 1] - b[v - 1]:
            neighbors[u - 1].append(v - 1)
    
    lengths = [len(lst) for lst in neighbors]
    strong = []
    i = 1
    for length in lengths:
        if length == n - 1:
            strong.append(str(i))
        i += 1
    print(len(strong))
    print(" ".join(strong))