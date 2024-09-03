from collections import deque
t = int(input())

for _ in range(t):
    string = list(input())
    n = len(string)
    new_string = deque()
    upper = deque()
    lower = deque()
    for i in range(n):
        if string[i] == "B":
            string[i] = ""
            if upper:
                string[upper.pop()] = ""
        elif string[i] == "b":
            string[i] = ""
            if lower:
                string[lower.pop()] = ""
        elif string[i].isupper():
            upper.append(i)
        else:
            lower.append(i)
    print("".join(string))