def check_board(board):
    for row in range(1, 7):
        for col in range(1, 7):
            if board[row - 1][col - 1] == board[row + 1][col + 1] == board[row + 1][col - 1] == board[row - 1][col + 1] == "#":
                return f"{row + 1} {col + 1}"

t = int(input())
for _ in range(t):
    blank = input()
    board = []
    for x in range(8):
        board.append([*input()])
    print(check_board(board))
