# https://codeforces.com/group/Sw3sdIlMPV/contest/315246/problem/C
num_sign_ups = int(input())
sign_ups = input().split()
num_attending = int(input())
attending = input().split()
all_names = set(sign_ups + attending)
present = 0
absent = 0
uninvited = 0

for name in all_names:
    if name in sign_ups and name in attending:
        # print(f"{name} is present!")
        present += 1
    elif name in sign_ups and name not in attending:
        # print(f"{name} is absent.")
        absent += 1
    elif name not in sign_ups:
        # print(f"What the heck is {name} doing here?!")
        uninvited += 1

print(present)
print(absent)
print(uninvited)