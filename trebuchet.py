import re

def get_end_digits(string):
    word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    # get first and last occurrence of words
    word_indices = []
    number_indices = []

    t = [] # a single letter list because I'm never going to use it again

    # find the first index with a match
    for w in word_digits:
        if w in string:
            e = string.index(w)
            if e != -1:
                t.append(e)
    
    if len(t) > 0:
        word_indices.append(min(t))

    # find the last index with a match
    t = []
    for r in word_digits:
        e = string.rfind(r)
        if e != -1:
            t.append(e)

    if len(t) > 0:
        word_indices.append(max(t))

    word_indices.sort()
    
    # get first and last occurrence of digits
    first = re.search(r'\d+', line)
    last = re.search(r'(\d+)(?!.*\d)', line)
    number_indices = []

    # just preventing any "'NoneType' object has no attribute 'span'" errors ;)
    if first:
        number_indices.append(first.span()[0])

    if last:
        number_indices.append(last.span()[-1])

    nums = []
    temp = [x for x in word_indices]
    temp.extend(number_indices)

    # account for cases where there is only one word
    if len(word_indices) == 1:
        word_indices = [word_indices[0], word_indices[0]]

    # if the smallest index is from word_indices, check which number is there
    if min(temp) in word_indices:
        for w in word_digits:
            if string.startswith(w, word_indices[0]):
                nums.append(str(word_digits.index(w) + 1))
                break
    else:
        nums.append(first.group()[0])

    # if the largest index is from word_indices, check which number is there
    if max(temp) in word_indices:
        for w in word_digits:
            if string.startswith(w, word_indices[-1]):
                nums.append(str(word_digits.index(w) + 1))
                break
    else:
        nums.append(last.group()[-1])

    # put the two numbers together :D
    return int("".join(nums))

with open("trebuchetinput.txt", "r") as f:
    s = 0
    for line in f:
        # Part 1
        '''
        first = re.search(r'\d+', line)
        last = re.search(r'(\d+)(?!.*\d)', line)
        s += int(first.group()[0] + last.group()[-1])
        '''

        # Part 2
        s += get_end_digits(line)
        # print(get_end_digits(line))
    print(s)