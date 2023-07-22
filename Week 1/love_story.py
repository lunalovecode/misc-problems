def check_diffs(word):
    ct = 0
    for i in range(10):
        if word[i] != "codeforces"[i]:
            ct += 1
    return ct

n = int(input())
for i in range(n):
    print(check_diffs(input()))