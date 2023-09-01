betters = int(input())
num_bets = []
bets = []
for _ in range(betters):
  num_bets.append(int(input()))
  bets.append([int(i) for i in input().split()])

x = int(input())

winners = []
winning_bets = []
i = 0
for bet in bets:
  if x in bet:
    winners.append(i)
    winning_bets.append(len(bet))
  i += 1

if winning_bets != []:
  least_bets = min(winning_bets)
  least_winners = []
  for w in winners:
    if num_bets[w] == least_bets:
      least_winners.append(str(w + 1))
  print(len(least_winners))
  print(" ".join(least_winners))
else:
  print(0)
  print()