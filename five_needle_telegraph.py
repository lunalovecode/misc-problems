# think of it as an actual square?
# make the diagonal the needles

n, m = [int(x) for x in input().split()]
grid = [["" for _ in range(n)] for _ in range(n)]

letters = []
for _ in range(2 * (n - 1)):
    letters.extend([*input()])

current_letter = 0
for c in range(n - 1, 0, -1):
    diagonal = c
    for r in range(n):
        if diagonal >= n:
            break
        grid[r][diagonal] = letters[current_letter]
        current_letter += 1
        diagonal += 1

current_letter = len(letters) - 1
for c in range(n - 1):
    diagonal = c
    for r in range(n - 1, -1, -1):
        if diagonal < 0:
            break
        grid[r][diagonal] = letters[current_letter]
        current_letter -= 1
        diagonal -= 1

def decode(grid, needles):
    for x in range(len(needles)):
        grid[x][x] = needles[x]
    
    i, j = -1, -1
    for row in range(n):
        for col in range(n):
            if grid[row][col] == "/":
                i = col
            elif grid[row][col] == "\\":
                j = col
            if i != -1 and j != -1:
                return grid[i][j]

message = []
for _ in range(m):
    message.append(decode(grid, input()))

print("".join(message))