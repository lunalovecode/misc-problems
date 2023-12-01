def solve(records):
    scores = [r[1] for r in records]
    records_without_lowest = [s for s in scores if s != min(scores)]
    second_lowest = min(records_without_lowest)
    names = []
    for r in records:
        if r[1] == second_lowest:
            names.append(r[0])
    names.sort()
    return names

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    for x in solve(records):
        print(x)