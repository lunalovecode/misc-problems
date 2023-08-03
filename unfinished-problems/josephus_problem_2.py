n, k = [int(x) for x in input().split()]
all = [x for x in range(1, n + 1)]
order = []
last = 0

def eliminate(people, k, index):
    if len(people) == 1:
        last = people[0]
        order.append(last)
        return last
    
    index = ((index + k) % len(people))
    a = people.pop(index)
    order.append(a)
    eliminate(people, k, index)

eliminate(all, k, 0)
print(" ".join([str(x) for x in order]))