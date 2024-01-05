# i'm memeing at this point
r, c = [int(x) for x in input().split()]
prev = []
all_moves = ["S" if x % 2 == 0 else "E" for x in range(r * c)]
# https://youtu.be/_B0CyOAO8y0
x = "S"
while True:
    print(x, flush=True)
    outcome = input()
    if not all_moves:
        print("RIGGED", flush=True)
        break
    prev.append(all_moves.pop(0))
    if outcome == "YAY":
        break
    else:
        if prev[-1] == "E":
            x = "S"
        else:
            x = "E"