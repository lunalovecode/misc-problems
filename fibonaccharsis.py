t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, n + 1):
        first = i
        second = n
        fibonacci_like = True
        for j in range(k - 2):
            first_2 = first
            first = second - first_2
            second = first_2
            fibonacci_like = fibonacci_like & (first <= second)
            fibonacci_like = fibonacci_like & (min(first, second) >= 0)
            if not fibonacci_like:
                break
        if fibonacci_like:
            ans += 1
    print(ans)