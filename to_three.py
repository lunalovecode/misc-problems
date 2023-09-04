n = int(input())
a = [x for x in str(n)]

def generate(nums, cur=[], ind=0):
    if ind == len(nums):
        return [cur[:]]

    cur.append(nums[ind])
    sub_with = generate(nums, cur, ind + 1)

    cur.pop()
    sub_without = generate(nums, cur, ind + 1)

    return sub_with + sub_without

all_nums = generate(a)
least_diff = 10000000000000000000 # 10^19
for x in all_nums:
    if len(x) <= len(a) and len(x) > 0 and sum([int(y) for y in x]) % 3 == 0:
        least_diff = min(least_diff, len(a) - len(x))

print(-1 if least_diff == 10000000000000000000 else least_diff)