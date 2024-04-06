string = input()
n = len(string)
temp = n * (n + 1) // 2

# is there a better way to do this?
so_far = []
for h in range(1,n + 1):
    for i in range(n - h + 1):
        j = i + h - 1

        lst = []
        for k in range(i,j + 1):
            lst.append(string[k])
        
        temp_str = "".join(lst)
        if temp_str not in so_far:
            so_far.append(temp_str)

print(len(so_far))