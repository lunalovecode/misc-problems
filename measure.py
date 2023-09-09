import math
def get_divisors(num):
  divisors = []
  for x in range(1, int(math.sqrt(num)) + 1):
    if num % x == 0:
      divisors.append(x)
      if x != num // x:
        divisors.append(num // x)
  divisors.sort()
  return divisors

n = int(input())
divisors = get_divisors(n)
satisfying_divisors = [[] for _ in range(n + 1)]
string = ["-" for _ in range(n + 1)]
for i in range(n + 1):
  for j in divisors:
    if 1 <= j <= 9 and i % (n / j) == 0:
      satisfying_divisors[i].append(j)

ind = 0
for x in satisfying_divisors:
  if len(x):
    string[ind] = str(min(x))
  ind += 1

print("".join(string))