from math import ceil

def generate_grid(r, c, m, k):
    added = 0
    grid = [["." for _ in range(c)] for _ in range(r)]
    if m < k:
        print("NO")
        return
    
    if m > r * c:
        print("NO")
        return

    if k > r * c:
        print("NO")
        return

    if k > min(r, c):
        print("NO")
        return
    
    if (ceil(m / k) * (k - 1)) <= 0:
        print("NO")
        return

    min_x, min_y = k, k

    if ceil(m / k) > k and (ceil(m / k) * k) <= r * c:
        min_y = ceil(m / k)
    
    x, y = min_x - 1, 0

    while x > 0:
        if y > min_y:
            break
        if added >= m:
            break
        grid[x][y] = "#"
        added += 1
        x -= 1
        y += 1

    i, j = 0, 0
    # '''    
    while added < m and i < min_x:
        if grid[i][j] == ".":
            grid[i][j] = "#"
            added += 1
        if j > min_y:
            j = 0
            i += 1
        else:
            j += 1

    # '''

    # how do i fill it in?
    '''
    b = False
    while i < min_x:
        while j < min_y:
            if grid[i][j] == ".":
                grid[i][j] = "#"
                added += 1
            if added >= m:
                b = True
                break
            j += 1
        if b == True:
            break
        i += 1
    '''

    print("YES")
    for g in grid:
        print("".join(g))


t = int(input())
for _ in range(t):
    r, c, m, k = [int(x) for x in input().split()]
    generate_grid(r, c, m, k)