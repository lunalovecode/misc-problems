o = [*input()]
e = [*input()]
string = []
i = 1
while len(e) > 0:
    if i % 2 == 0:
        a = e.pop(0)
        string.append(a)
    else:
        b = o.pop(0)
        string.append(b)
    i += 1

if len(o) == 1:
    string.append(o[0])

print("".join(string))