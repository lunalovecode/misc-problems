t = int(input())
a = []

def rnd(n):
    maximum = 0
    a = n
    for i in range(len(str((n))) + 2):
        if a > maximum:
            maximum = a

        if str(n)[-1] == "5":
            a = round(a + 1, i * -1)
        else: 
            a = round(a, i * -1)

    return maximum

for _ in range(t):
    n = input()
    num = int(n)
    a.append(rnd(num))

for b in a:
    print(b)
