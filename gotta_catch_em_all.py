string = input()
bulbasaur = {"B": 1, "u": 2, "l": 1, "b": 1, "a": 2, "s": 1, "r": 1}
string_bulbasaur = {b: string.count(b) for b in "Bulbasaur"}
# find a better solution after this
# B >= 1
# u >= 2
# l >= 1
# b >= 1
# a >= 2
# s >= 1
# r >= 1

ans = 1
for b in string_bulbasaur:
    if string_bulbasaur[b] < bulbasaur[b]:
        ans = 0
        break

lst = [string_bulbasaur[b] for b in bulbasaur]

if ans == 1:
    m = max(lst)
    for i in range(m, 0, -1):
        temp = [bulbasaur[b] * i for b in bulbasaur]
        ct = 0
        for j in range(7):
            if lst[j] >= temp[j]:
                ct += 1
        if ct == 7:
            ans = i
            break

print(ans)