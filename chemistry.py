"""
For future reference
def can_be_palindrome(string):
    if len(string) % 2 == 0:
        for letter in set(string):
            if string.count(letter) != 2:
                return False
        return True
    else:
        odd_letter_counts = 0
        for letter in set(string):
            if string.count(letter) % 2 != 0:
                odd_letter_counts += 1
        
        if odd_letter_counts > 1:
            return False
        
        return True
"""

def with_removed_characters(string, n, k):
    odd_letter_counts = 0
    for x in set(string):
        if string.count(x) % 2 != 0:
            odd_letter_counts += 1

    
    return odd_letter_counts <= k + 1


t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    print("YES" if with_removed_characters(input(), n, k) else "NO")