#metehan 12 phred hw
import math

def char_to_prob(char):
    p = ord(char) - 33
    if p < 0: return None
    return 10 ** (-p / 10)

def prob_to_char(prob):
    if prob <= 0 or prob > 1: return None
    p= -10 * math.log10(prob)
    return chr(int(p)+33)
print(char_to_prob('A'))
print(prob_to_char(0.001))
print(prob_to_char(2))