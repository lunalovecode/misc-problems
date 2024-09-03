t = int(input())
for _ in range(t):
    n, k, start, end = [int(x) for x in input().split()]
    coords = {}
    for i in range(n):
        coords[i + 1] = tuple([int(x) for x in input().split()])

    cost = abs(coords[start][0] - coords[end][0]) + abs(coords[start][1] - coords[end][1])
    if k == 0:
        print(cost)
        continue
    major_from_start = min([abs(coords[start][0] - coords[i][0]) + abs(coords[start][1] - coords[i][1]) for i in range(1, k + 1)])
    major_from_end = min([abs(coords[end][0] - coords[i][0]) + abs(coords[end][1] - coords[i][1]) for i in range(1, k + 1)])

    cost = min(cost, major_from_start + major_from_end)
    print(cost)