n = int(input())
duties = input()

def abc_in_duties():
    for i in range(n - 2):
        x = [duties[i], duties[i + 1], duties[i + 2]]
        x.sort()
        if x == ["A", "B", "C"]:
            return True
    return False

ans = 2

if n >= 2:
    if duties[-1] != duties[-2]:
        ans = 1
    if n >= 3:
        if abc_in_duties():
            ans = 0

print(ans)