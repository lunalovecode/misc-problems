n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]

for num in nums:
    m = num % k
    if m == 0:
        print(num // k, sep=" ")