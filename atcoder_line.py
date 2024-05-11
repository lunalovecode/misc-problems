n, x, y, z = [int(x) for x in input().split()]

if z in range(x, y) or z in range(y, x):
    print("Yes")
else:
    print("No")