def count_days(schedules):
    cts = []
    ct = 0
    if len(schedules) == 1:
        for x in schedules[0]:
            if x == "o":
                ct += 1
            else:
                cts.append(ct)
                ct = 0
        if ct > 0:
            cts.append(ct)
    else:
        for schedule in zip(*schedules):
            if all(sched == "o" for sched in schedule):
                ct += 1
            else:
                cts.append(ct)
                ct = 0
        if ct > 0:
            cts.append(ct)
    return max(cts)

n, d = [int(x) for x in input().split()]
scheds = []
for _ in range(n):
    scheds.append(input())

print(count_days(scheds))