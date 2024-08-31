r1, c1, r2, c2 = [int(x) for x in input().split()]
rook_moves = 0
bishop_moves = 0
king_moves = 0

diff_rows = abs(r1 - r2)
diff_cols = abs(c1 - c2)
# rook needs 2 moves max
if r1 != r2:
    rook_moves += 1

if c1 != c2:
    rook_moves += 1

# bishop is complicated
# same diagonal
if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
    bishop_moves = 1
    king_moves = diff_rows
elif ((r1 % 2 == c1 % 2) == (r2 % 2 == c2 % 2)) or ((r1 % 2 == r2 % 2) == (c1 % 2 == c2 % 2)):
    bishop_moves = 2

# if they're on the same color square, max moves is 2


# it's always possible with the king, but the moves are even harder to count
if r1 == r2:
    king_moves = diff_cols
elif c1 == c2:
    king_moves = diff_rows
else:
    king_moves = max(diff_rows, diff_cols)


# i forgot search algorithms weee
# max moves is 
# (5, 5) (2, 4)
# diff_rows = 3, diff_cols = 1
# max is 3
# oh wait never mind

print(rook_moves, bishop_moves, king_moves)