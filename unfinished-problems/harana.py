n = int(input())
song = [int(x) for x in input().split()]
bob = [int(x) for x in input().split()]

def offkeyness(notes_1, notes_2):
    return sum([abs(a - b) for a, b in zip(notes_1, notes_2)])

# O(n)
def optimal_key(notes_1, notes_2):
    diffs = [b - a for a, b in zip(notes_1, notes_2)]
    k = 0
    min_offkey = 10000
    for d in diffs:
        o = offkeyness(notes_2, [x + d for x in notes_1])
        if o < min_offkey:
            k = d
            min_offkey = o
    return k

# O(n)
# get the new song after the key changes
def key_change(notes_1, notes_2, m):
    k1 = optimal_key(notes_1[0:m], notes_2[0:m])
    k2 = optimal_key(notes_1[m:], notes_2[m:])
    new_song = []
    for i in range(m):
        new_song.append(notes_1[i] + k1)
    
    for i in range(m, len(notes_1)):
        new_song.append(notes_1[i] + k2)
    
    return new_song

ans = []

# key_change = O(n)
# offkeyness = O(n)
# loop = O(n)
# O(n^3)???
# measure the new song's offkeyness when compared to Bob's singing
for i in range(1, n):
    ans.append(str(offkeyness(bob, key_change(song, bob, i))))

print(" ".join(ans))