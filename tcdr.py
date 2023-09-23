s = input()
t = [x for x in s if x not in "aeiou"]
print("".join(t))