with open("hauntedwastelandinput.txt") as f:
    configuration = {}
    instructions = ""
    for line in f:
        if instructions == "":
            instructions = line.rstrip()
        elif line == "\n":
            continue
        else:
            point, points = [y.rstrip() for y in line.split(" = ")]
            points = [x for x in points.split(", ")]
            points = [points[0][1:4], points[1][0:3]]
            configuration[point] = points

    current = "AAA"
    
    steps = 0
    while current != "ZZZ":
        for x in instructions:
            if x == "L":
                current = configuration[current][0]
            elif x == "R":
                current = configuration[current][1]
            steps += 1
    print(steps)
    