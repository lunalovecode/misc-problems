digits = "314159265358979323846264338327"
n = int(input())
ct = 0
for _ in range(n):
    num = input()
    for i in range(len(num)):
        if num[i] == digits[i]:
            ct += 1
        elif i + 1 > 30:
            break
        else:
            break
    print(ct)
    ct = 0