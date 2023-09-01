n = int(input())
s = [*input()]
q = int(input())
for _ in range(q):
  x = [i for i in input().split()]
  if x[0] == "1":
    s[int(x[1]) - 1] = x[2]
  elif x[0] == "2":
    s = [i.lower() for i in s]
  else:
    s = [i.upper() for i in s]

print("".join(s))