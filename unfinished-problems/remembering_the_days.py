import itertools
num_towns, num_roads = [int(x) for x in input().split()]
roads = []
road_lengths = []
town_nums = []
for _ in range(num_roads):
    road = [int(x) for x in input().split()]
    x = [road[0], road[1]]
    x.sort()
    roads.append(x)
    road_lengths.append(road[2])

for road in roads:
    town_nums.extend(road)

def valid_path(path):
    a = False
    if len(path) < 2:
        return False
    prev = path[0]
    for x in path[1:]:
        y = [prev, x]
        y.sort()
        if y in roads:
            a = True
        else:
            return False
        prev = x
    return a

def path_length(path):
    prev = path[0]
    length = 0
    for x in path[1:]:
        y = [prev, x]
        y.sort()
        length += road_lengths[roads.index(y)]
        prev = x
    return length

town_nums = list(set(town_nums))
valid_paths = []
for i in range(2, num_towns + 1):
    valid_paths.extend([list(x) for x in itertools.permutations(town_nums, i) if valid_path(x)])

all_lengths = []
for p in valid_paths:
    all_lengths.append(path_length(p))
print(max(all_lengths))