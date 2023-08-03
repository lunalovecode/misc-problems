import numpy

n = int(input())
A = []
B = []
for _ in range(n):
    A.append([int(x) for x in input().split()])

for _ in range(n):
    B.append([int(x) for x in input().split()])

A = numpy.array(A)
B = numpy.array(B)
print(numpy.dot(A, B))