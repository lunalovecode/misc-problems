def construct_square(n, first, c, d):
    square = [[0] * n for _ in range(n)]
    square[0][0] = first
    for i in range(n - 1):
        for j in range(n - 1):
            square[i + 1][j] = square[i][j] + c
            square[i][j + 1] = square[i][j] + d
    square[n - 1][n - 1] = square[n - 2][n - 1] + c
    return square

def flatten(square):
    new = []
    for s in square:
        new += s
    return new

t = int(input())
for _ in range(t):
    n, c, d = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    nums.sort()
    sq = flatten(construct_square(n, nums[0], c, d))
    sq.sort()
    print("YES" if nums == sq else "NO")