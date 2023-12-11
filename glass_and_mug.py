k, g, m = [int(x) for x in input().split()]
glass, mug = 0, 0

for _ in range(k):
    if glass == g:
        glass = 0
    elif mug == 0:
        mug = m
    else:
        if mug <= (g - glass):
            glass += mug
            mug = 0
        else:
            mug -= (g - glass)
            glass = g

print(glass, mug)