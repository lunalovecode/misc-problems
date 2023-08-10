string = input()
if all(a.islower() for a in string[::2]) and all(a.isupper() for a in string[1::2]):
    print("Yes")
else:
    print("No")