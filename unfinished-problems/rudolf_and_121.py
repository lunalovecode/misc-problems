def operation(a, i):
    b = [x for x in a]
    b[i - 1] -= 1
    b[i] -= 2
    b[i + 1] -= 1
    return b

b = [1, 2, 1, 3, 4, 3]
operation(b, 1)
operation(b, 4)
print(b)

# recursion?
def func(a):
    # if every element is 0, return "YES"
    # else, use recursion and operate on each index
    # if any element becomes negative, return "NO"
    if all([x == 0 for x in a]):
        return "YES"
    else:
        for i in range(1, len(a) - 1):
            x = operation(a, i)
            print(x)
            print(any([y < 0 for y in x]))
            if any([y < 0 for y in x]):
                continue
            else:
                func(x)

print(func([1, 3, 5, 5, 2]))