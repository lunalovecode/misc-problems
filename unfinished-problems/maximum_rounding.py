# t = int(input())

def rnd(n):
    a = [*n]
    largest_leftmost_digit = "-1"
    # find leftmost digit >= 5
    ind = -1
    for d in a:
        if int(d) >= 5:
            largest_leftmost_digit = d
            ind = a.index(d)
            break
    
    
    # add 1 to the digit to the left
    # replace rightmost digits with 0
    

    # return "".join(a)

# print(rnd("20445"))
a = rnd("20445")
'''
for _ in range(t):
    n = input()
    a.append(n)
'''