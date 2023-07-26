n = int(input())
s = input()
A, B, C = False, False, False
ct = 0
for char in s:
    ct += 1
    if char == "A" and A == False:
        A = True
    elif char == "B" and B == False:
        B = True
    elif char == "C" and C == False:
        C = True
    else:
        continue
        
    if all([A, B, C]):
        break
print(ct)