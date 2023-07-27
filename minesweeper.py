def valid(i, j, n, m):
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1

def get_adjacent(arr, i, j):
    n = len(arr)
    m = len(arr[0])
 
    v = []
 
    if (valid(i - 1, j - 1, n, m)):
        v.append(arr[i - 1][j - 1])
    if (valid(i - 1, j, n, m)):
        v.append(arr[i - 1][j])
    if (valid(i - 1, j + 1, n, m)):
        v.append(arr[i - 1][j + 1])
    if (valid(i, j - 1, n, m)):
        v.append(arr[i][j - 1])
    if (valid(i, j + 1, n, m)):
        v.append(arr[i][j + 1])
    if (valid(i + 1, j - 1, n, m)):
        v.append(arr[i + 1][j - 1])
    if (valid(i + 1, j, n, m)):
        v.append(arr[i + 1][j])
    if (valid(i + 1, j + 1, n, m)):
        v.append(arr[i + 1][j + 1])
 
    return v

h, w = [int(x) for x in input().split()]
grid = []
grid_with_nums = grid
for _ in range(h):
    grid.append([*input()])

for x in range(h):
    for y in range(w):
        if grid[x][y] != "#":
            num_bombs = get_adjacent(grid, x, y).count("#")
            grid_with_nums[x][y] = str(num_bombs)

for line in grid_with_nums:
    print("".join(line))