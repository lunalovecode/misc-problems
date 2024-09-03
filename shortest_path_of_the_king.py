s = input()
t = input()
start = ("abcdefgh".index(s[0]), int(s[1]))
end = ("abcdefgh".index(t[0]), int(t[1]))

# get differences between coords
current = [start[0], start[1]]
moves = []
while tuple(current) != end:
    current_move = ""
    if current[0] < end[0]:
        current[0] += 1
        current_move += "R"
    elif current[0] > end[0]:
        current[0] -= 1
        current_move += "L"
    if current[1] < end[1]:
        current[1] += 1
        current_move += "U"
    elif current[1] > end[1]:
        current[1] -= 1
        current_move += "D"
    moves.append(current_move)

print(len(moves))
for m in moves:
    print(m)