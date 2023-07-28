def can_talk(vlad_height, heights, k, max_diff):
    # if the absolute value of the difference is a multiple of k
    # and that it is not greater than the max possible difference
    # and that the difference is not 0 (meaning they are the same height and will have to share a step, which is not allowed)
    # they can talk
    ct = 0
    for height in heights:
        diff = abs(vlad_height - height)
        if diff % k == 0 and diff <= max_diff and diff != 0:
            # print(f"{diff} is greater than or equal to {max_diff}")
            ct += 1
    # print(ct)
    return ct

t = int(input())
res = []
for _ in range(t):
    n, m, k, h = [int(x) for x in input().split()]
    heights = [int(x) for x in input().split()]
    can_talk(h, heights, k, (m * k) - k)
    res.append(can_talk(h, heights, k, (m * k) - k))

for r in res:
    print(r)