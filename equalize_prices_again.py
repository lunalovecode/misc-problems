from math import ceil
t = int(input())
for _ in range(t):
    n = int(input())
    items = [int(x) for x in input().split()]
    print(ceil(sum(items) / n))