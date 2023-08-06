t = int(input())
for _ in range(t):
    a, b = [x for x in input().split()]
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as z:
        print(f"Error Code: {z}")
    except ValueError as v:
        print(f"Error Code: {v}")