n = int(input())
for _ in range(n):
    ticket = [int(x) for x in input()]
    if sum(ticket[0:3]) == sum(ticket[3:6]):
        print("YES")
    else:
        print("NO")