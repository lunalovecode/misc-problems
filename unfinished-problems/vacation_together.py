# keep track of common sequences of os between 1 and 2
# - if there is only 1 person given for whatever reason, print the longest sequence of os present
# check if any of those sequences exist in 3
# if it does, check for common sequences between 3 and 4
# check if any of those exist in 5
# repeat the process
# if, at any point, none do, print 0 and lament about how all of your friends have more activities than your lazy butt will ever be willing to--
# i meant busy. how busy your friends are.
"""
xooox
oooxx
oooxo

1[1:3] = 2[1:3]
2[1:3] = 3[1:3]

oxooooooooooooo
oxooxooooooooox
oxoooooooooooox
oxxxooooooxooox
oxooooooooxooox
1[2:3] = 2[2:3]
2[2:3] = 3[2:3]
3[2:3] != 4[2:3]

1[5:13] = 2[5:13]
2[5:13] != 3[5:13]

1[5:9] = 2[5:9]
2[5:9] = 3[5:9]
3[5:9] = 4[5:9]
4[5:9] = 5[5:9]
"""

def count_matching_positions(*strings):
    if not strings:
        raise ValueError("No strings provided for comparison.")

    length = len(strings[0])
    count = 0

    for chars_at_same_index in zip(*strings):
        if len(set(chars_at_same_index)) == 1:
            count += 1

    return count

# Example usage:
string1 = "xooox"
string2 = "oooxx"
string3 = "xooox"

result = count_matching_positions(string1, string2, string3)
print(result)  # Output: 2


