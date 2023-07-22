# https://www.youtube.com/watch?v=ldrjCgsJWgg
# Use prime factorization
# get the products of the combinations of those factors

import math, itertools
prime_factors = []

def prime_factor(n):
    while n % 2 == 0:
        prime_factors.append(2)
        n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n /= i

    if n > 2:
        prime_factors.append(n)

def powerset(items):
    l_items = list(items)
    return itertools.chain.from_iterable(itertools.combinations(l_items, r) for r in range(len(l_items) + 1))

n = int(input())
prime_factor(n)
print(prime_factors)
l = list(powerset(prime_factors))