from collections import deque

def count_elements(lst_1, lst_2):
    return len([i for i in range(len(lst_1)) if lst_1[i] == lst_2[i]])

n = int(input())
first = deque([int(x) for x in input().split()])
second = deque([int(x) for x in input().split()])

max_matches = 0
for _ in range(n):
    first.rotate(1)
    a = count_elements(first, second)
    if a > max_matches:
        max_matches = a
    if max_matches == n:
        break
    

print(max_matches)