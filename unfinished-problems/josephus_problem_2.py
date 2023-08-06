from collections import deque
n, k = [int(x) for x in input().split()]
all = deque([x for x in range(1, n + 1)])
order = []

start = 0
while len(all) > 0:
    start %= len(all)
    to_remove = (start + k) % len(all)
    start = to_remove
    t = all[to_remove]
    order.append(str(t))
    all.remove(t)

print(" ".join(order))