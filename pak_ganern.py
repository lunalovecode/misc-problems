def pak_ganern(n):
    sequence = []
    for i in range(n):
        for _ in range(i):
            if len(sequence) >= n:
                return sequence
            sequence.append("PAK")
        for _ in range(i):
            if len(sequence) >= n:
                return sequence
            sequence.append("GANERN")
    return sequence

for x in pak_ganern(int(input())):
    print(x)