n = int(input())
for _ in range(n):
    nums = [int(x) for x in input().split()]
    nums.remove(min(nums))
    if nums[0] + nums[1] >= 10:
        print("YES")
    else:
        print("NO")