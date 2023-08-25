t = int(input())

def rnd(n):
    ind = -1
    for d in n:
        if d >= 5:
            ind = n.index(d)
            break
    
    if ind == -1:
        return "".join([str(x) for x in n])
    
    i = ind
    
    if ind == 0:
        n.insert(0, 1)
        i = 1
    else:
        n[ind - 1] += 1

    for d in range(i, len(n)):
        n[d] = 0
    
    if sum([1 for x in n if x >= 5]):
        # What do you call this type of recursion again?
        return rnd(n)
    else:
        return "".join([str(x) for x in n])

a = []
for _ in range(t):
    n = [int(x) for x in input()]
    a.append(rnd(n))

# for readability purposes in testing
for x in a:
    print(x)