#metehan oglio melting temperature assignment

def tm(a, c, g, t):
    total = a + c + g + t
    if total <=13:
        return (a + t) * 2 + (g + c) * 4 #uses this formula if total is <=13
    else:
        return 64.9 +41 * (g + c - 16.4) / total #uses this if greater
print(tm(5,7,3,4))
print(tm(15,17,13,14))
