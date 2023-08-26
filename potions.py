num_potions, health, min_health = [int(x) for x in input().split()]
potions = [int(x) for x in input().split()]
effective_potions = []
for potion in potions:
    if potion + health >= min_health:
        effective_potions.append(potion)

print(potions.index(min(effective_potions)) + 1)