def is_beautiful(mat):
    # please forgive me
    return mat[0][0] < mat[0][1] and mat[1][0] < mat[1][1] and mat[0][0] < mat[1][0] and mat[0][1] < mat[1][1]

def rotate(m):
    return list(zip(*m[::-1]))

n = int(input())
for _ in range(n):
    matrix = []
    for i in range(2):
        matrix.append([int(x) for x in input().split()])
    ninety = rotate(matrix)
    one_eighty = rotate(ninety)
    two_seventy = rotate(one_eighty)
    rotations = [matrix, ninety, one_eighty, two_seventy]
    if any(list(map(is_beautiful, rotations))):
        print("YES")
    else:
        print("NO")