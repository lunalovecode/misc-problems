t = int(input())
def divide(pile, target):
    if pile == target:
        return True
    elif pile % 3 != 0:
        return False
    else:
        return divide(pile // 3, target) or divide((2 * pile) // 3, target)

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    print("YES" if divide(n, m) else "NO")