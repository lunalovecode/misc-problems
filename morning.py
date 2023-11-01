t = int(input())
for _ in range(t):
    n = input()
    seconds = 0
    prev = 1
    for d in n:
        d = int(d)
        diff = abs(prev - d)
        
        if d == prev == 0:
            diff = 0
        elif d == 0:
            diff = 10 - prev
        elif prev == 0:
            diff = 10 - d
        
        seconds += diff + 1
        prev = d

    print(seconds)