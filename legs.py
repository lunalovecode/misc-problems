# divide by 4
# if mod 4 = 2, add 1
t = int(input())
for _ in range(t):
    n = int(input())
    total = n // 4
    if n % 4 == 2:
        total += 1
    print(total)