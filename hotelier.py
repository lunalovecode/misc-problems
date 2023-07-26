status = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
nearest_unoccupied_left = 0
nearest_unoccupied_right = 9
n = int(input())
events = [*input()]
# if it is "L", check the nearest unoccupied room from 0
# if it is "R", check the nearest unoccupied room from 9

for event in events:
    if event == "L":
        if nearest_unoccupied_left != None:
            status[nearest_unoccupied_left] = "1"
    elif event == "R":
        if nearest_unoccupied_right != None:
            status[nearest_unoccupied_right] = "1"
    else:
        status[int(event)] = "0"
    nearest_unoccupied_left = status.index("0") if "0" in status else None
    nearest_unoccupied_right = "".join(status).rfind("0") if "0" in status else None

print("".join(status))