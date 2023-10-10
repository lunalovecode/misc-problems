pan = dict()
pam = dict()
pang = dict()
patinig = dict()
hiram = dict()

n = int(input())
names = [x for x in input().split()]
for name in names:
    if name[0] in "dlrst":
        pan[name] = name
    elif name[0] in "bp":
        pam[name] = name
    elif name[0] in "ghkmnwy":
        pang[name] = name
    elif name[0] in "aeiou":
        patinig[name] = name
    else:
        hiram[name] = name
    
print(*sorted(pan.values()))
print(*sorted(pam.values()))
print(*sorted(pang.values()))
print(*sorted(patinig.values()))
print(*sorted(hiram.values()))