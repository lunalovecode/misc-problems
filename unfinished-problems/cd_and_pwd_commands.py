n = int(input())
directory = []
for _ in range(n):
    command = input().split()
    if command[0] == "pwd":
        if len(directory) == 0:
            print("/")
        else:
            print(f"{'/'.join(directory)}/")
    else:
        path = [x for x in command[1].split("/")]
        if ".." not in path:
            directory = path
        else:
            for p in path:
                if p == "..":
                    directory.pop()
                elif p != "":
                    directory.append(p)
            
            directory = [x for x in directory if (len(x) != 0 and x != "/")]

        if len(directory) != 0:
            if not directory[0].startswith("/"):
                directory[0] = f"/{directory[0]}"
            if directory[0] == "/":
                directory.pop(0)
                directory[0] = f"/{directory[0]}"
        
        print(f"\n{directory}")