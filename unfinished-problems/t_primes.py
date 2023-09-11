import math
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
x = ["YES" if len(get_factors(int(num))) == 3 else "NO" for num in input().split()]
for y in x:
    print(y)