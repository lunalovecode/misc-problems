k, n, w = [int(x) for x in input().split()]
bananas_cost = (w * (w + 1)) // 2
debt = (bananas_cost * k) - n
print(debt if debt > 0 else 0)