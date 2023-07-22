t = int(input())
for _ in range(t):
    n = int(input())
    to_n = [i for i in range(1, n + 1)]
    seq = []
    for i in range(n):
        p = [int(x) for x in input().split()]
        seq.append(str(abs(sum(to_n) - sum(p))))
    print(" ".join(seq))