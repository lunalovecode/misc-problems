s = input()
t = input()

len_s = len(s)
len_t = len(t)

inds = []
i, j, = 0, 0
while i < len_s and j < len_t:
    if s[i] == t[j]:
        i += 1
        inds.append(j + 1)
    j += 1

print(" ".join([str(x) for x in inds]))