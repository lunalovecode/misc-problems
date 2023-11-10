def solve(rounds):
    wins = dict()
    for i in range(0, len(rounds)):
        wins[i + 1] = rounds[i].count("o")
    wins = sorted(wins.items(), key=lambda x:x[1], reverse=True)
    players = []
    for w in wins:
        players.append(str(w[0]))
    return " ".join(players)

n = int(input())
rounds = []
for i in range(n):
    rounds.append(input())

print(solve(rounds))