#metehan 26 death saves hw
import random
def character_in_peril():
    successes = 0
    failures = 0
    while True:
        roll = random.randint(1,20)
        if roll == 20: return 'r'
        elif roll == 1:
            failures += 2
        elif roll < 10:
            failures += 1
        elif roll >= 10:
            successes += 1
        
        if failures >= 3: return 'd'
        if successes >= 3: return 's'
    

trials = 50000

deaths = 0
stables = 0
revives = 0
for i in range(trials):
    status = character_in_peril()
    if status == 'd':
        deaths += 1
    elif status == 's':
        stables += 1
    elif status == 'r':
        revives += 1
        
print(deaths/trials)
print(stables/trials)
print(revives/trials)
