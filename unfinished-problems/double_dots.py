rooms, passages = [int(x) for x in input().split()]
adjacency = [[] for _ in range(rooms)]

for _ in range(passages):
    a, b = [int(x) for x in input().split()]
    adjacency[a - 1].append(b - 1)
    adjacency[b - 1].append(a - 1)

def search(start, adjacency, rooms):
    visited = [False for _ in range(rooms)]
    visited[start] = True
    queue = [start]
    prev = [-1 for _ in range(rooms)]
    dists = [1000 for _ in range(rooms)]
    dists[start] = 0
    prev[start] = -1
    ct = 0

    while ct < len(queue):
        current = queue[ct]
        for a in adjacency[current]:
            if not visited[a]:
                visited[a] = True
                dists[a] = dists[current] + 1
                prev[a] = current
                queue.append(a)
        ct += 1
    
    return prev

def shortest_path(start, prev):
    path = []
    while start != -1:
        path.append(start)
        start = prev[start]
    return path

ans = "Yes"
signs = []
for i in range(1, rooms):
    d = shortest_path(i, search(0, adjacency, rooms))
    if len(d) < 2:
        ans = "No"
        break
    else:
        signs.append(d[1] + 1)

print(ans)
if ans == "Yes":
    for sign in signs:
        print(sign)