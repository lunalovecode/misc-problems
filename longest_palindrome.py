def is_palindrome(string):
    for x in range(len(string)):
        if len(string) % 2 != 0 and x == len(string) // 2 + 1:
            continue
        elif string[x] != string[len(string) - (x + 1)]:
            return False
    return True

string = input()
max_len = 1
start, end = 0, len(string)
while start <= end:
    s = "".join([string[x] for x in range(start, end)])
    if is_palindrome(s):
        max_len = max(max_len, len(s))
    if end - 1 == start:
        end = len(string)
        start += 1
    end -= 1

print(max_len)