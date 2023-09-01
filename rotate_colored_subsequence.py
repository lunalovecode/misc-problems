n, m = [int(x) for x in input().split()]
s = [*input()]
colors = [int(x) for x in input().split()]
chars_by_color = [[] for i in range(m)]
indices_by_color = [[] for i in range(m)]
for i in range(n):
  chars_by_color[colors[i] - 1].append(s[i])
  indices_by_color[colors[i] - 1].append(i)

for j in range(m):
  chars_by_color[j] = chars_by_color[j][-1:] + chars_by_color[j][:-1]

new_s = [*s]
i = 0
for k in indices_by_color:
  j = 0
  
  for l in k:
    new_s[l] = chars_by_color[i][j]
    j += 1
  
  i += 1

print("".join(new_s))