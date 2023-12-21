from math import inf
n, k = [int(x) for x in input().split()]
heights = [int(x) for x in input().split()]

memo = [inf for _ in range(n)]
memo[0] = 0

for i in range(n):
    for j in range(1, k + 1):
        if i + j < n:
            memo[i + j] = min(memo[i + j], memo[i] + abs(heights[i + j] - heights[i]))

print(memo[-1])