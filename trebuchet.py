import re

def get_end_digits(string):
    word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    # get first and last occurrence of words
    word_indices = []
    number_indices = []

    temp_matches = []
    for w in word_digits:
        if w in string:
            e = string.index(w)
            if e != -1:
                temp_matches.append(e)
    
    if len(temp_matches) > 0:
        word_indices.append(min(temp_matches))

    temp_matches = []
    for r in word_digits:
        e = string.rfind(r)
        if e != -1:
            temp_matches.append(e)


    if len(temp_matches) > 0:
        word_indices.append(max(temp_matches))

    word_indices.sort()
    
    # get first and last occurrence of digits
    first = re.search(r'\d+', line)
    last = re.search(r'(\d+)(?!.*\d)', line)
    number_indices = []
    if first:
        number_indices.append(first.span()[0])
    if last:
        number_indices.append(last.span()[-1])
    nums = []
    temp = [x for x in word_indices]
    temp.extend(number_indices)
    if min(temp) in word_indices:
        for w in word_digits:
            if string.startswith(w, word_indices[0]):
                nums.append(str(word_digits.index(w) + 1))
                break
    else:
        nums.append(first.group()[0])
    
    if len(word_indices) == 1:
        word_indices = [word_indices[0], word_indices[0]]

    if max(temp) in word_indices:
        for w in word_digits:
            if string.startswith(w, word_indices[-1]):
                nums.append(str(word_digits.index(w) + 1))
                break
    else:
        nums.append(last.group()[-1])

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
        print(get_end_digits(line))
    print(s)