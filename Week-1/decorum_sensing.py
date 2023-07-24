n = int(input())
shynesses = [int(x) for x in input().split()]
shynesses.sort()
thank_yous = 0
for shyness in shynesses:
    if shyness <= thank_yous:
        thank_yous += 1
print(thank_yous)