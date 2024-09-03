n, t = [int(x) for x in input().split()]
queue = input()

new_queue = [q for q in queue]
prev_queue = [q for q in queue]
for i in range(t):
    for j in range(n - 1):
        # print(f"the current lineup is {prev_queue}")
        if prev_queue[j] == "B":
            # print(f"the {j}th person is a boy")
            if prev_queue[j + 1] == "G":
                new_queue[j] = "G"
                new_queue[j + 1] = "B"
                # print(f"the new lineup is {new_queue}\n")
            # else:
                # print("there are no girls directly behind him\n")
        else:
            # print(f"the {j}th person is a girl\n")
            continue
    # print(f"the queue went from {prev_queue} to {new_queue}")
    prev_queue = [n for n in new_queue] # python gets a little quirky
 
print("".join(new_queue))