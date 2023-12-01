n, s = int(input()), input().split()
print(all([int(x) > 0 for x in s]) and any([x == x[::-1] for x in s]))