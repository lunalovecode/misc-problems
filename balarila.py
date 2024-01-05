# lol
def vowel(letter):
    if letter in ["a", "e", "i", "o", "u"]:
        return True
    return False


# get all the valid consonant combinations in the word and how many times they appear
valid = {}
def get_valid(word, length):
    for i in range(length - 1):
        x, y = word[i], word[i + 1]

        if vowel(x) or vowel(y):
            continue

        if x == y:
            continue
        
        s = "".join([x, y])
        if s not in valid:
            valid[s] = 1
        else:
            valid[s] += 1
word = input()
n = len(word)
new_letters = ["NO"] * n

get_valid(word, n)
# find the first combination that is NOT in the word
def find_last():
    consonants = "bcdfghjklmnpqrstvwxyz"
    for i in range(21):
        for j in range(21):
            if consonants[i] == consonants[j]:
                continue
            s = "".join([consonants[i], consonants[j]])
            if s not in word:
                new_letters[-1] = s
                return

find_last()

for i in range(n - 1):
    # get the ith and i + 1th character
    x, y = word[i], word[i + 1]
    
    # if either x and y are vowels, skip
    if vowel(x) or vowel(y):
        continue
    
    # if x and y are the same, skip
    if x == y:
        continue
    
    s = "".join([x, y])
    ind = n - valid[s] - 1
    
    if new_letters[ind] == "NO":
        # set the answer when k = ind
        new_letters[ind] = s
    else:
        # get the lexicographically smaller between the old answer and the new
        new_letters[ind] = min(new_letters[ind], s)

print(" ".join(new_letters))