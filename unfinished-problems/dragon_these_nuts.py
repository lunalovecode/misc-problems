n, k = [int(x) for x in input().split()]
roast_times = [int(x) for x in input().split()]
nuts = {}

for i, el in enumerate(roast_times):
    nuts[str(i + 1)] = el

# it stands for Power Point. you're so dirty minded smh
def pp_cost(nuts):
    # return the biggest of the nuts
    return max(nuts)

# put the second largest at position k
