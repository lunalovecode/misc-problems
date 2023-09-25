def count_points(target):
    points = 0
    for x in range(10):
        for y in range(10):
            if target[x][y] == "X":
                if 4 <= x <= 5 and 4 <= y <= 5:
                    points += 5
                elif 3 <= x <= 6 and 3 <= y <= 6:
                    points += 4
                elif 2 <= x <= 7 and 2 <= y <= 7:
                    points += 3
                elif 1 <= x <= 8 and 1 <= y <= 8:
                    points += 2
                else:
                    points += 1

    return points


t = int(input())
for _ in range(t):
    target = []
    for _ in range(10):
        target.append([*input()])
    print(count_points(target))