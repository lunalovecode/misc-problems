def median(a,x):
    lst = []
    for i in range(len(x)):
        if a[i] == "r":
            if x[i] not in lst or len(lst) == 1:
                print("Wrong!")
            else:
                lst.remove(x[i])
                lst.sort()
                print((lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2 if len(lst) % 2 == 0 else lst[len(lst) // 2])
        else:
            lst.append(x[i])
            lst.sort()
            print((lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2 if len(lst) % 2 == 0 else lst[len(lst) // 2])
            

N = int(input())
s = []
x = []
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
median(s,x)