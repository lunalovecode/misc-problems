t = int(input())
for _ in range(t):
    n = int(input())
    responses = {}
    for i in range(n):
        words, quality = [int(x) for x in input().split()]
        if words <= 10:
            responses[str(i + 1)] = quality
    response_nums = list(responses.keys())
    qualities = list(responses.values())
    ind = qualities.index(max(qualities))
    print(response_nums[ind])