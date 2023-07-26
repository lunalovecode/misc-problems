n = int(input())
words = []
for _ in range(n):
    word = []
    for _ in range(8):
        line = [*input()]
        for char in line:
            if char.isalpha():
                word.append(char)
    words.append("".join(word))

for word in words:
    print(word)