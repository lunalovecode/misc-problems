def combos(lst, n=6):
    if n == 0:
        return [[]]

    l = []

    for i in range(0, len(lst)):
        m = lst[i]
        r = lst[i + 1:]
    
        remaining_combo = combos(r, n-1)
        for p in remaining_combo:
            l.append([m, *p])
           
    return l

queries = []

while True:
    i = [int(x) for x in input().split()]
    
    if i[0] == 0:
        break
    else:
        queries.append(i)

query_count = 0
for query in queries:
    s = query[1:]
    for combo in combos(s):
        print(" ".join([str(x) for x in combo]))
    
    if query_count != len(queries) - 1:
        print()
    query_count += 1