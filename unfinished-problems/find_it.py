n = int(input())
nums = [int(x) for x in input().split()]
connections = [[] for _ in range(n)]
ct = 1
for num in nums:
    connections[num - 1].append(ct - 1)
    ct += 1

print(connections)