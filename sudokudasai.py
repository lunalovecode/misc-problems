# Kawaii~
grid = []
for _ in range(9):
    grid.append([int(x) for x in input().split()])

# check each row if all of the integers from 1 to 9 is present
def valid_row(r):
    return all(i in r for i in range(1, 10))

# check each column if all of the integers from 1 to 9 from present
def valid_col(c):
    col = [grid[r][c] for r in range(0, 9)]
    return all(i in col for i in range(1, 10))

# check each subgrid if all of the integers from 1 to 9 from present
def valid_subgrid(subgrid_row, subgrid_col):
    vals = grid[subgrid_row][subgrid_col: subgrid_col + 3]
    vals.extend(grid[subgrid_row + 1] [subgrid_col: subgrid_col + 3])
    vals.extend(grid[subgrid_row + 2] [subgrid_col: subgrid_col + 3])
    return all(i in vals for i in range(1, 10))

all_rows_valid = all(list(map(valid_row, grid)))
all_columns_valid = []
all_subgrids_valid = []

for i in range(9):
    all_columns_valid.append(valid_col(i))

all_cols_valid = all(all_columns_valid)

for j in range(0, 9, 3):
    all_subgrids_valid.append(valid_subgrid(j, j))

all_sgs_valid = all(all_subgrids_valid)

if all_rows_valid and all_cols_valid and all_sgs_valid:
    print("SUDOKUDASAI")
else:
    print("SUDOKUNAI")