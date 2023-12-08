# Part 1
def is_possible(rounds):
    for rnd in rounds:
        for play in rnd.split(", "):
            x = play.split()
            num = int(x[0])
            color = x[1]
        
            if (color == "red" and num > 12) or (color == "green" and num > 13) or (color == "blue" and num > 14):
                return False
    return True

# Part 2
def get_power(rounds):
    red = []
    green = []
    blue = []
    for rnd in rounds:
        for play in rnd.split(", "):
            x = play.split()
            num = int(x[0])
            color = x[1]

            if color == "red":
                red.append(num)
            elif color == "green":
                green.append(num)
            else:
                blue.append(num)
    
    return max(red) * max(green) * max(blue)

with open("cubeconundruminput.txt", "r") as f:
    # Part 1
    id_num = 1
    s = 0
    for line in f:
        l = line.split(": ")
        rounds = l[1].split("; ")
        
        # Part 1
        '''
        if is_possible(rounds):
            s += id_num
        id_num += 1
        '''

        s += get_power(rounds)


    print(s)

