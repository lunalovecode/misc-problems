from math import *
def distance(point_coords, center_coords):
    x, y = point_coords[0], point_coords[1]
    h, k = center_coords[0], center_coords[1]
    equation = ((x - h) * (x - h)) + ((y - k) * (y - k))
    return sqrt(equation)

n, h, k = [int(x) for x in input().split()]
center_coords = (h, k)
all_coords = []
for _ in range(n):
    all_coords.append(tuple(float(x) for x in input().split()))

farthest = -inf
for coord in all_coords:
    farthest = max(farthest, distance(coord, center_coords))

print(farthest * 2)