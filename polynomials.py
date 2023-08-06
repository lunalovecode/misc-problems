import numpy
P = [float(x) for x in input().split()]
x = int(input())

print(numpy.polyval(P, x))