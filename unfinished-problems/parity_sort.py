# if the difference between the number of evens and the number of odds is no more than 1
# or if all items have the same parity
# or if there is only one item
# print "YES"
# we can sort, we can shuffle, we can...

def diff_between_parities(lst):
    even, odd = 0, 0
    patt = []
    for num in lst:
        if num % 2 == 0:
            even += 1
            patt.append("E")
        else:
            odd += 1
            patt.append("O")

    if (len(patt) == 1 or abs(even - odd) <= 1) or (len(set(patt[::2])) == 1) and (len(set(patt[1::2])) == 1):
        return "YES"
    else:
        return "NO"

t = int(input())
res = []
for _ in range(t):
    n = int(input())
    # print(diff_between_parities([int(x) for x in input().split()]))
    res.append(diff_between_parities([int(x) for x in input().split()]))

for r in res:
    print(r)