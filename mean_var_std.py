import numpy
arr = []
n, m = [int(x) for x in input().split()]

for _ in range(n):
    arr.append([int(x) for x in input().split()])

arr = numpy.array(arr)
print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(round(numpy.std(arr), 11))