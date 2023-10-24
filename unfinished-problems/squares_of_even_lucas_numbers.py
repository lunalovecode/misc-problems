# n, m = 30, 1000
# 900

n, m = (10**6) + 2023, 998244353
# n, m = 9, 5
# n, m = 100, 2023
# not 589980868
# not 589980872

L = [None for _ in range(n)]
L[0] = 2
L[1] = 1
s = 4 # because 2^2 = 4
for k in range(2, n):
    L[k] = (L[k - 1] + L[k - 2])
    if L[k] % 2 == 0:
        s += (L[k] % m ** 2)

# print(L[k])
print(s % m)