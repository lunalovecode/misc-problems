n = int(input())
a = []
for _ in range(n):
    b = [*input()]
    b.sort()
    a.append("".join(b))

print(a)
def find_substring(lst):
    s = lst[0]
    l = len(s)
    ans = ""
    for i in range(l):
        for j in range(i + 1, l + 1):
            sub = s[i:j]
            k = 1
            for k in range(1, n):
                if sub not in lst[k]:
                    break
            
            if (k + 1 == n and len(ans) < len(sub)):
                ans = sub
    
    return ans

print(find_substring(a))