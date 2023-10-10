n = int(input())
rook_count = 0
board = []
ans = "NO"
for _  in range(n):
    line = input()
    board.append(line)
    rook_count += line.count("R")
    if line.count("R") > 1:
        ans = "YES"

def is_attacking(board):
    for i in range(len(board)):
        col = [board[r][i] for r in range(len(board))]
        if board[i].count("R") > 1 or col.count("R") > 1:
            return "YES"
    return "NO"

ans = is_attacking(board)
print(rook_count)
print(ans)