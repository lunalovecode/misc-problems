n = int(input())
all = [x for x in range(1, n + 1)]
order = []

while len(all) > 1:
    remaining = []
    for i in range(len(all)):
        if i % 2 == 1:
            order.append(all[i])
        else:
            remaining.append(all[i])
    
    if len(all) % 2 == 0:
        all = remaining
    else:
        start = remaining.pop()
        all.clear()
        all.append(start)
        for r in remaining:
            all.append(r)

order.append(all[0])
print(" ".join([str(x) for x in order]))