n = int(input())
lst = []
for _ in range(n):
    num = input()
    if num not in lst:
        lst.append(num)
    else:
        lst.remove(num)
    
print(len(lst))