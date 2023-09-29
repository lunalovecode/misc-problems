t = int(input())
for _ in range(t):
    n = int(input())
    wheel = [int(x) for x in input().split()]
    new_wheel = [*wheel]
    for i in range(n):
        operations = [x for x in input().split()]
        for j in range(int(operations[0])):
            if operations[1][j] == "D":
                if new_wheel[i] == 9:
                    new_wheel[i] = 0
                else:
                    new_wheel[i] += 1
            else:
                if new_wheel[i] == 0:
                    new_wheel[i] = 9
                else:
                    new_wheel[i] -= 1
    print(" ".join([str(x) for x in new_wheel]))