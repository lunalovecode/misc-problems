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

def with_removed_characters(string, k):
    # are all of the letters unique?
    if sorted(list(set(string))) == sorted([x for x in string]):
        return False
    return True

print(can_be_palindrome(input()))