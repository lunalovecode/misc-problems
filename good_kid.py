import functools
t = int(input())
for _ in range(t):
    n = int(input())
    presents = [int(x) for x in input().split()]
    added = False
    for x in range(n):
        if presents[x] == min(presents) and added == False:
            presents[x] += 1
            added = True
    
    print(functools.reduce(lambda a, b: a * b, presents))