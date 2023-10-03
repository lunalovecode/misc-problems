n = int(input())
dists = [abs(int(x)) for x in input().split()]
manhattan = sum(dists)
euclidian = sum([x ** 2 for x in dists]) ** 0.5
chebyshev = max(dists)
print(manhattan)
print(euclidian)
print(chebyshev)