n = int(input())
people = [int(x) for x in input().split()]
other_people = [p for p in people]
p_1 = other_people.pop(0)
strongest = max(people)
if p_1 == strongest and (not any(person == p_1 for person in other_people)):
    print(0)
else:
    print(strongest - p_1 + 1)