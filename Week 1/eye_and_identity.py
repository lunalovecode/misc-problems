import numpy
numpy.set_printoptions(legacy="1.13")
n, m = [int(x) for x in input().split()]

print(numpy.eye(n, m))