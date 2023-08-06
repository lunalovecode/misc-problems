import math
def flip(start, end):
    start_to_end = string[start:end+1]
    for c in range(len(start_to_end)):
        start_to_end[c] = 1 - start_to_end[c]
    new_str = [*string]
    new_str[start:end+1] = start_to_end
    return new_str

t = int(input())
b = []
for _ in range(t):
    n = int(input())
    string = [*input()]
    string = [int(x) for x in string]
    best = math.inf
    for i in range(n):
        for j in range(i, n):
            best = min(best, sum(flip(i, j)))
    b.append(best)

for i in b:
    print(i)