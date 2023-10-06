n = int(input())
marks = sorted([int(x) for x in input().split()])
classmates = sorted([int(x) for x in input().split()])

if all([y >= x for x, y in zip(marks, classmates)]):
    print("YES")
else:
    print("NO")