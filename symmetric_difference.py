m = int(input())
a = set([int(x) for x in input().split()])
n = int(input())
b = set([int(x) for x in input().split()])

c, d = a.difference(b), b.difference(a)
e = set()
e.update(c, d)
e = list(e)
e.sort()
for f in e:
    print(f)