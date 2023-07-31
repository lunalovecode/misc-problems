import numpy

n, m = [int(x) for x in input().split()]
array = []

for _ in range(n):
    array.append([int(x) for x in input().split()])

array = numpy.array(array)

arr_sum = numpy.sum(array, axis = 0)
print(numpy.prod(arr_sum))