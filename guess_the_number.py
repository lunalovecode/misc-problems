lower, upper = 1, 1000000
while lower != upper:
    mid = (lower + upper + 1) // 2
    print(mid, flush=True)
    feedback = input()
    if feedback == "<":
        upper = mid - 1
    else:
        lower = mid
    
print(f"! {lower}", flush=True)