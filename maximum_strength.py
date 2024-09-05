def pad(string, n):
    new = ["0"] * (n - len(string))
    new += string
    return new

t = int(input())
for _ in range(t):
    l, r = [list(x) for x in input().split()] # l <= r < 10^100 just means there are going to be 100 digits at most :)
    l = pad(l, len(r))
    if l == r:
        print(0)
        continue
    
    diff = -1
    for i in range(len(r)):
        if l[i] != r[i]:
            diff = i
            break
    
    # cant brute force this
    # get as many 9s and 0s as possible
    print((int(r[diff]) - int(l[diff])) + (9 * (len(r) - diff - 1)))