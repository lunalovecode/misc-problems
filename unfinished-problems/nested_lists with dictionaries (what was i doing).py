if __name__ == '__main__':
    records = []
    rec_obj = {}
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        names.append(name)
        scores.append(score)
        rec_obj = dict(zip(names, scores))
        
    next_smallest = None
    rev_scores = scores
    rev_scores.sort(reverse=True)
    lowest = min(scores)
    for i in rev_scores:
        if i == lowest:
            break
        if next_smallest == None or i < next_smallest:
            next_smallest = i
    
    indices = []
    for indx, value in enumerate(scores):
        if value == next_smallest:
            indices.append(indx)
    
    sorted_rec_obj = sorted(rec_obj.items(), key=lambda x:x[1])
    
    lst = []
    for j in indices:
        lst.append(sorted_rec_obj[j - 1][0])
        lst.sort()
    
    for k in lst:
        print(k)
