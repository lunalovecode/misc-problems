# Diabetes Simulator
t = int(input())
for _ in range(t):
    n = int(input())
    boxes = [int(x) for x in input().split()]
    least = min(boxes)
    eat = 0
    for box in boxes:
        eat += abs(box - least)
    print(eat)