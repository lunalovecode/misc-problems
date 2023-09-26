n = int(input())
for _ in range(n):
    size_1, size_2 = [x for x in input().split()]
    ans = "="
    if "S" in size_1 and any([x in size_2 for x in ["M", "L"]]):
        ans = "<"
    elif "M" in size_1 and "L" in size_2:
        ans = "<"
    elif "S" in size_2 and any([x in size_1 for x in ["M", "L"]]):
        ans = ">"
    elif "M" in size_2 and "L" in size_1:
        ans = ">"
    elif "S" in size_1 and "S" in size_2 and size_1.count("X") > size_2.count("X"):
        ans = "<"
    elif "S" in size_1 and "S" in size_2 and size_1.count("X") < size_2.count("X"):
        ans = ">"
    elif "L" in size_1 and "L" in size_2 and size_1.count("X") > size_2.count("X"):
        ans = ">"
    elif "L" in size_1 and "L" in size_2 and size_1.count("X") < size_2.count("X"):
        ans = "<"
    print(ans)