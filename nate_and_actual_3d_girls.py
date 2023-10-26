def shift(s, k):
    new_str = []
    for char in s:
        if char.isalpha():
            if char.isupper() and ord(char) + (k % 26) > ord("Z"):
                new_str.append(chr(ord("A") + (ord(char) + k % 26) - ord("Z") - 1))
            elif char.islower() and ord(char) + (k % 26) > ord("z"):
                new_str.append(chr(ord("a") + (ord(char) + k % 26) - ord("z") - 1))
            else:
                new_str.append(chr(ord(char) + (k % 26)))
        else:
            new_str.append(char)
    return "".join(new_str)

n, m, k = [int(x) for x in input().split()]
cards = "".join(input().split())
tegami = "".join(input().split())
encrypted = shift(tegami, k)
ans = "Make her kokoro go doki-doki!"
card_letter_counts = dict()
tegami_letter_counts = dict()
all_letter_counts = card_letter_counts
all_letter_counts.update(tegami_letter_counts)

for x in set(cards):
    card_letter_counts[x] = cards.count(x)

for x in set(encrypted):
    tegami_letter_counts[x] = encrypted.count(x)

for x in tegami_letter_counts:
    try:
        if card_letter_counts[x] < tegami_letter_counts[x]:
            ans = "It is gonna be daijoubu."
            break
    except KeyError:
        ans = "It is gonna be daijoubu."
        break

print(ans)