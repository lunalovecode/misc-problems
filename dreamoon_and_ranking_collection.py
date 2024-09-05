t = int(input()) # 1 <= t <= 5?
for _ in range(t):
    n, extra_rounds = [int(x) for x in input().split()]
    places = sorted(set([int(x) for x in input().split()]))
    ans = 0
    ct = 0
    for i in range(1, n + extra_rounds + 1):
        if ct == extra_rounds:
            break
        if i not in places:
            ans = i
            ct += 1

    # check places starting from ans
    # if the difference between the ith element and the element before that is equal to 1, set ans to the ith element
    prev = ans
    for i in range(ans + 1, len(places)):
        if places[i] -  places[prev] == 1:
            ans = places[i]
        else:
            break
        prev = i
    
    for i in range(ans, max(places)):
        if i + 1 in places:
            ans = i + 1
        else:
            break
    
    print(ans)
    # print(f"{_ + 1}: {ans}")

'''
1
5 2
3 4 5 6 7

'''