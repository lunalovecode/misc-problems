t = int(input())

def check_rows(grid):
    for row in grid:
        if all(square == "X" for square in row):
            return "X"
        elif all(square == "O" for square in row):
            return "O"
        elif all(square == "+" for square in row):
            return "+"
    return None

def check_cols(grid):
    col_1 = [i[0] for i in grid]
    col_2 = [i[1] for i in grid]
    col_3 = [i[2] for i in grid]
    grid_cols = [col_1, col_2, col_3]
    return check_rows(grid_cols)

def check_diags(grid):
    if (grid[0][0] == grid[1][1] == grid[2][2]) and grid[0][0] != ".":
        return grid[0][0]
    if (grid[2][0] == grid[1][1] == grid[0][2]) and grid[2][0] != ".":
        return grid[2][0]

res = []
for _ in range(t):
    grid = []
    for _ in range(3):
        row = [*input()]
        grid.append(row)

    if check_rows(grid):
        res.append(check_rows(grid))
    elif check_cols(grid):
        res.append(check_cols(grid))
    elif check_diags(grid):
        res.append(check_diags(grid))
    else:
        res.append("DRAW")

for r in res:
    print(r)
