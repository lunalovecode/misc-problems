n = int(input()) % 1000037

'''
x = 0
for i in range(1, n + 1):
    x += (i ** 2) % 1000037

print(f"For loop computation: {x % 1000037}")
print(f"Formula: {((n * (n + 1) * ((2 * n) + 1)) // 6) % 1000037}")
'''

print(((n * (n + 1) * ((2 * n) + 1)) // 6) % 1000037)

# n = 10
# n = 10000
# n = 14348907
# n = 202300000000000000?