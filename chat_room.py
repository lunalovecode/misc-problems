def is_subsequence(subsequence, string):
    n, m, i, j = len(subsequence), len(string), 0, 0
    while i < n and j < m:
        if subsequence[i] == string[j]:
            i += 1
        j += 1
    
    return i == n

string = input()
print("YES" if is_subsequence("hello", string) else "NO")