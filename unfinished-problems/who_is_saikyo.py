# if a number appears twice in the same position, print -1
# otherwise, find [a, b], [b, c], [c, d]...
# then append a, b, c, d... to a list
# if this list includes every number (and that no number appears more than once in the same position), print a.

n, m = [int(x) for x in input().split()]
superiorities = []

def sort_key(sub_list):
    return sub_list[1]

for _ in range(m):
    superiorities.append([int(x) for x in input().split()])

chain = []
for x, y in zip(superiorities[0::], superiorities[1::]):
    if x[0] == y[0] or x[1] == y[1]:
        print(-1)
        break

print(chain)