import math
# This function has NO RIGHT to be that fast
def get_factors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)
    factors.sort()
    return factors

n = int(input())
factors = get_factors(n)
for factor in factors:
    print(factor)