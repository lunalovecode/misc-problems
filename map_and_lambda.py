cube = lambda x: x ** 3

def fibonacci(n):
    sequence = []
    i = 0
    while i < n:
        if len(sequence) == 0:
            sequence.append(0)
        elif len(sequence) == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])
        i += 1
    
    return sequence

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))