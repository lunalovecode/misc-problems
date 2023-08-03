n, passing_grade = [int(x) for x in input().split()]
grades = [int(x) for x in input().split()]
failures = [grade for grade in grades if grade < passing_grade]
print(len(failures))