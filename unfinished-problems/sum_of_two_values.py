n, x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
solution = []
for b in a:
    if abs(b - x) in a:
        solution.append(str(a.index(b) + 1))
        solution.append(str(a.index(abs(b - x)) + 1))
        break

if len(solution) == 0:
    print("Impossible")
else:
    print(" ".join(solution))