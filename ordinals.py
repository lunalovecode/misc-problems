n = int(input())
def ordinal(num):
    suffix = "th"
    if num % 10 == 1 and num % 100 != 11:
        suffix = "st"
    elif num % 10 == 2 and num % 100 != 12:
        suffix = "nd"
    elif num % 10 == 3 and num % 100 != 13:
        suffix = "rd"
    
    return f"{num}{suffix}"

print(ordinal(n))