from math import inf
from heapq import *

i = inf
n, m = [int(x) for x in input().split()]
adj = [[] for _ in range(n)]
queue = [(0, 0)]
dists = [0] + [i] * n
prev = [-1] * n
for _ in range(m):
    u, v, w = [int(x) for x in input().split()]
    adj[u - 1] += [(w, v - 1)]
    adj[v - 1] += [(w, u - 1)]

while queue:
    u = heappop(queue)[1]
    for a in adj[u]:
        w, v = dists[u] + a[0], a[1]
        if w < dists[v]:
            dists[v] = w
            prev[v] = u
            heappush(queue, (dists[v], v))

if dists[n - 1] == i:
    print(-1)
else:
    x, path = n - 1, []
    while x != -1:
        path.append(x + 1)
        x = prev[x]
    path.reverse()
    print(" ".join([str(x) for x in path]))