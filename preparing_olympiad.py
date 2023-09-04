def valid(lst, l, r, x):
    if len(lst) >= 2 and sum(lst) >= l and sum(lst) <= r and max(lst) - min(lst) >= x:
        return True
    else:
        return False

def generate(nums, cur=[], ind=0):
    if ind == len(nums):
        return [cur[:]]

    cur.append(nums[ind])
    sub_1 = generate(nums, cur, ind + 1)

    cur.pop()
    sub_2 = generate(nums, cur, ind + 1)

    return sub_1 + sub_2

n, l, r, x = [int(i) for i in input().split()]
problems = [int(i) for i in input().split()]
all_sets = generate(problems)
ct = 0
for s in all_sets:
    if valid(s, l, r, x):
        ct += 1

print(ct)