t = int(input())
for _ in range(t):
    n = int(input())
    none_count = 0
    first = []
    second = []
    both = []
    for _ in range(n):
        time, skills = input().split()
        time = int(time)
        if skills == "00":
            none_count += 1
        elif skills == "10":
            first.append(time)
        elif skills == "01":
            second.append(time)
        else:
            both.append(time)
    min_first = min(first) if first else 1000000000
    min_second = min(second) if second else 1000000000
    min_both = min(both) if both else 1000000000
    res = (min_first + min_second if min_first + min_second < min_both else min_both)
    if none_count == n:
        res = -1
    if res == 1000000000:
        res = -1
    print(res)