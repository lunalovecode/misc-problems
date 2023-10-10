import math
n, m = [int(x) for x in input().split()]
students = dict()
good_noodles = dict()
super_good_noodles = dict()

for x in range(1, n + 1):
    students[x] = 0

for _ in range(m):
    a = int(input())
    attended = [int(x) for x in input().split()]
    for at in attended:
        students[at] += 1

student_list = list(students)

for student in student_list:
    if students[student] >= math.ceil(m / 2):
        good_noodles[student] = student
    if students[student] == m:
        super_good_noodles[student] = student

print(len(good_noodles))
print(*sorted(good_noodles))
print(len(super_good_noodles))
print(*sorted(super_good_noodles))