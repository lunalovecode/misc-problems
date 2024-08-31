n = int(input())
queen_x, queen_y = [int(x) for x in input().split()]
king_x, king_y = [int(x) for x in input().split()]
target_x, target_y = [int(x) for x in input().split()]

ans = "YES"
if queen_x in range(min(king_x, target_x), max(king_x, target_x)):
    ans = "NO"

if queen_y in range(min(king_y, target_y), max(king_y, target_y)):
    ans = "NO"

print(ans)