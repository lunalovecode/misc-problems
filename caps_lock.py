def caps_lock(string):
    new_string = []
    for c in string:
        if c.isupper():
            new_string.append(c.lower())
        else:
            new_string.append(c.upper())
    return "".join(new_string)

string = input()
if all([x.isupper() for x in string]) or (all([x.isupper() for x in string[1::]]) and string[0].islower()):
    print(caps_lock(string))
else:
    print(string)