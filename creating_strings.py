def get_permutations(string, i):
    if i == len(string):
        permutations.append("".join(string))
    else:
        for j in range(i, len(string)):
            string[i], string[j] = string[j], string[i]
            get_permutations(string, i + 1)
            string[j], string[i] = string[i], string[j]

string = input()
permutations = []
get_permutations([*string], 0)
permutations = list(set(permutations))
permutations.sort()
print(len(permutations))
for p in permutations:
    print(p)