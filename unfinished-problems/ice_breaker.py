# get shortest distance
from math import inf
n, m = [int(x) for x in input().split()]
names = [x for x in input().split()]
adj = [[] for _ in range(n)]

for _ in range(m):
    k = int(input())
    y = ""
    for x in input().split():
        if y != "":
            adj[names.index(x)].append(names.index(y))
            adj[names.index(y)].append(names.index(x))
        y = x

def search(n, dest, adj, dists, prev):
    dists = [inf for _ in range(n)]
    prev = [-1 for _ in range(n)]
    queue = [0]
    visited = [False for _ in range(n)]
    visited[0] = True
    dists[0] = 0

    while len(queue) != 0:
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):
            if not visited[adj[u][i]]:
                visited[adj[u][i]] = True
                dists[adj[u][i]] = dists[u] + 1
                prev[adj[u][i]] = u
                queue.append(adj[u][i])

                if adj[u][i] == dest:
                    return True
    return False

def get_alice_num(adj, dest, n):
    prev = [0 for _ in range(n)]
    alice_nums = [0 for _ in range(n)]
    path = []
    crawl = dest
    path.append(crawl)

    if not search(n, dest, adj, alice_nums, prev):
        return -1
    while prev[crawl] != -1:
        path.append(prev[crawl])
        crawl = prev[crawl]
        
    return str(alice_nums[dest])

print(adj)
print(get_alice_num(adj, 2, n))