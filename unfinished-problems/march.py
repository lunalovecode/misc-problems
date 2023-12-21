from math import factorial
n = int(input())
march_counts = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for _ in range(n):
    name = input()
    if name[0] in "MARCH":
        march_counts[name[0]] += 1

available = 0
for m in march_counts:
    if march_counts[m] > 0:
        available += 1

combinations = factorial(available) // (factorial(3) * factorial(abs(3 - available)))
total_combinations = combinations
for m in march_counts:
    print(total_combinations)
    if march_counts[m] > 0:
        total_combinations *= march_counts[m]

print(available, combinations, march_counts)
print(total_combinations)