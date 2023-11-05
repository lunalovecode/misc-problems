n = int(input())
s = input()
ans = "No"
for i in range(n - 1):
    if sorted([s[i], s[i + 1]]) == ["a", "b"]:
        ans = "Yes"
        break
print(ans)