#Metehan saving throws hw 24

import random

trials = 10
def roll_d20():
    return random.randint(1, 20)

def success_chance(dc, trials):
    success = 0
    for i in range(trials):
        if roll_d20() >= dc:
            success += 1
    return success / trials

def advantage_chance(dc, trials):
    success = 0
    for i in range(trials):
        r1 = roll_d20()
        r2 = roll_d20()
        if (r1 if r1 > r2 else r2) >= dc:  #Taking the higher roll
            success += 1
    return success / trials

def disadvantage_chance(dc, trials):
    success = 0
    for i in range(trials):
        r1 = roll_d20()
        r2 = roll_d20()
        if (r1 if r1 < r2 else r2) >= dc:  #taking the lower roll
            success += 1
    return success / trials

print("DC Normal Advantage Disadvantage") #table

for dc in [5, 10, 15]: #computing for different DC's
    normal = success_chance(dc, trials)
    adv = advantage_chance(dc, trials)
    disadv = disadvantage_chance(dc, trials)
    
    print(dc, " ", round(normal, ndigits=2), " ", round(adv, ndigits=2), " ", round(disadv, ndigits=2))