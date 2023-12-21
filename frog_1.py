from math import inf
n = int(input())
heights = [int(x) for x in input().split()]

memo = [inf for _ in range(n)]
memo[0] = 0
memo[1] = abs(heights[0] - heights[1])

for i in range(2, n):
    hop_1 = abs(heights[i] - heights[i - 1]) + memo[i - 1]
    hop_2 = abs(heights[i] - heights[i - 2]) + memo[i - 2]
    memo[i] = min(hop_1, hop_2)

print(memo[-1])