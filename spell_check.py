x = ['T', 'i', 'm', 'r', 'u']
t = int(input())
for _ in range(t):
    n = int(input())
    s = [x for x in input()]
    if n != 5:
        print("NO")
    elif sorted(s) != x:
        print("NO")
    else:
        print("YES")