animals, legs = [int(x) for x in input().split()]
ans = "Yes"
# if legs is greater than animals * 4, return no
# the maximum number of legs for A animals is A * 4, where all of the animals are turtles
if legs > animals * 4:
    ans = "No"

# if legs is less than animals * 2 (or if legs is less than animals), return no
# the minimum number of legs for A animals is A * 2, where all of the animals are cranes
if legs < animals * 2:
    ans = "No"
if legs < animals:
    ans = "No"

# if legs is odd, return no because both cranes and turtles have an even number of legs
if legs % 2 != 0:
    ans = "No"

print(ans)