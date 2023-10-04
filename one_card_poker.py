a, b = [int(x) for x in input().split()]
if (not (a == 13 and b == 1) and a > b) or (a == 1 and b == 13):
    print("Alice")
elif a == b:
    print("Draw")
else:
    print("Bob")