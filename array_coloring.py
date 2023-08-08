t = int(input())
for _ in range(t):
    n = int(input())
    lst = [int(x) for x in input().split()]
    print("YES" if sum(lst) % 2 == 0 else "NO")