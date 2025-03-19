#Metehan entropy.py

import sys
import math #lines 6-10 harvest words on the command line and turn them into probabilities

probs = [] #sets up a container to hold the probabulities used for the calculation
for arg in sys.argv[1:]: #steps through each argument (word) on the command line, using a slice sys.argv[1:] to skip over the first argument, which is the name of the program.
    f = float(arg) #converts the argument into a floating point number
    if f <= 0 or f >= 1: sys.exit('error: not a probability') # checks to see if the number is a valid probability. The numbers 0 and 1 are considered illegal in this context because values of 0 cause numerical errors (log(0) and there is no point in calculating the entropy of a single value of 1.0)
    probs.append(f) #adds each floating point number to the container of probabilities.

total = 0 #Lines 12-15check if the sum of the probabilities on the command line are equal to 1.0. Of course, we never ask if floating point values are actually equal to anything, so we check if they sum nearly to 1.0.
for p in probs: total += p
if not math.isclose(total, 1.0):
    sys.exit('error: probs must sum to 1.0')

h = 0 #calculate entropy.
for p in probs:
    h -= p * math.log2(p) #reports the final value using an f-string

print(f'{h:.4f}')

""" Running the program
python3 31entropy.py 0.5 0.5
python3 31entropy.py 0.25 0.25 0.25 0.25
python3 31entropy.py 0.4 0.3 0.2 0.1
python3 31entropy.py 0.5 0.6
python3 31entropy.py 0.5 -1
"""