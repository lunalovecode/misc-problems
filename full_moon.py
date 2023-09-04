n, m, p = [int(x) for x in input().split()]

lower_bound = 1 + (-m) / p
upper_bound = 1 + (n - m) / p
num_terms = int(upper_bound) - int(lower_bound)

print(num_terms)