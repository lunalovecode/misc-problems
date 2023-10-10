prizes = dict()
prize_1_name = input()
prize_1_val = int(input())
prizes[prize_1_name] = prize_1_val
prize_2_name = input()
prize_2_val = int(input())
prizes[prize_2_name] = prize_2_val
prize_3_name = input()
prize_3_val = int(input())
prizes[prize_3_name] = prize_3_val

prize_list = list(prizes)

ans = "NO"
p = None
for x in prize_list:
    other_prizes = list(prizes.values())
    other_prizes.remove(prizes[x])
    if prizes[x] > sum(other_prizes):
        ans = "YES"
        p = x
        break

print(ans)
if p != None:
    print(p)