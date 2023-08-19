n = int(input())
for _ in range(n):
    words = [x for x in input().split()]
    new_words = [*words]
    for i in range(len(words)):
        a = 0
        try:
            a = int(words[i]) if (len(words[i]) > 1 and words[i][0] != "0") or (len(words[i]) == 1) else words[i]
            new_words[i] = str(a - 1)
        except:
            continue
    print(" ".join(new_words))