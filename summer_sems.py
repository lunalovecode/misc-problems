import math
def generate(n, m):
    result = 2023
    results = [2023]
    for i in range(2, n + 1):
        result = (2024 * result + 1521) % m
        results.append(result)
    return results

def factorial(n):
    res = n
    for i in range(n - 1, 0, -1):
        res *= i
    return res

def inverse(n):
    m = 998244353
    return (pow(3, n, m) - 1) * ((m + 1) // 2) % m

n = int(input())
# n = 5
# 692388931

# n = 1600
# 136761437

# n = 16000
# 478320439

# n = 16000000
# 564485394

m = 998244353

a = generate(n, m)
n_fac = factorial(n) % m
inverses = [inverse(x) for x in range(1, n + 1)]
ans = 0
'''
for l in range(1, n):
    subtotal = 0
    for r in range(l, n):
        subtotal += a[r]
        subtotal %= m
        
        ans += subtotal * inverses[r - l + 1] % m
        ans %= m
'''

c = 0
d = None

for i in range(n // 2):
    if i == 1:
        d = sum(inverses)
    else:
        d -= inverses[i - 1]
        d -= inverses[n - (i - 1) + 1]
    
    c += d
    ans += a[i] * c % m
    ans += a[n - i + 1] * c % m
    ans %= m
        

print(ans * n_fac % m)