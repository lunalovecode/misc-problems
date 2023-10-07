import math
pi = math.pi
maguire_pizzas = int(input())
maguire_diameter = int(input())
total_maguire_area = (pi * ((maguire_diameter / 2) ** 2)) * maguire_pizzas
holland_pizzas = int(input())
holland_diameter = int(input())
total_holland_area = (pi * ((holland_diameter / 2) ** 2)) * holland_pizzas

if total_maguire_area > total_holland_area:
    print("Maguire's Pizza")
elif total_holland_area > total_maguire_area:
    print("Holland's Pizza")
else:
    print("Garfield's Lasagna")