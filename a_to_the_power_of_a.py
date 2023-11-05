b = int(input())
# a ** a gets big really quick, so the loop won't run for too long
for a in range(1, b + 1):
    if a ** a == b:
        print(a)
        break
    elif a ** a > b:
        print(-1)
        break