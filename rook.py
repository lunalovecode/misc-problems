def move_possibilities(pos):
    col, row = [*pos]
    row = int(row)
    for i in range(1, row):
        print(f"{col}{i}")
    
    for i in range(row + 1, 9):
        print(f"{col}{i}")
    
    for i in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        if i != col:
            print(f"{i}{row}")

t = int(input())
for _ in range(t):
    move_possibilities(input())