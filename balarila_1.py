salita = input()
unlapi = "pang"
if salita[0] in "dlrst":
    unlapi = "pan"
elif salita[0] in "pb":
    unlapi = "pam"
elif salita[0] in "aeiou":
    unlapi = "pang-"

print(f"{unlapi}{salita}")