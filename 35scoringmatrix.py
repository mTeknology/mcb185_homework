#Metehan 35scoringmatrix.py homework

import sys


nts = sys.argv[1] #Put nucleotides first
match = sys.argv[2] #Match point
mismatch = sys.argv[3] #Mismatch point

print(" ", end="  ")
for nt in nts:
    print(nt, end="  ")
    
print('')




for nt1 in nts:
    print(nt1, end=" ")
    for nt2 in nts:
        if nt1 == nt2:
            print(match, end=' ')
        else:
            print(mismatch, end=' ')
            
    print('')
    