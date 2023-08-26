n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
prev = nums[0] - 1
for num in nums:
    if num - prev != 1:
        print(prev + 1)
        break
    prev = num