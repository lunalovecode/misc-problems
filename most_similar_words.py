# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
def get_diff(word_1, word_2, l):
    diff = 0
    for x in range(l):
        diff += abs(ord(word_1[x]) - ord(word_2[x]))
    
    return diff

t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    words = []
    diff = 1000000000
    for _ in range(n):
        words.append(input())
    
    for i in range(n):
        for j in range(i + 1, n):
            diff = min(diff, get_diff(words[i], words[j], m))
    
    print(diff)