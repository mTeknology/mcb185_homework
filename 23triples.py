#Metehan 23triples.py homework 

for a in range(1, 100): #iterating over range of less than 100. Starts at 1
    for b in range(a, 100):  #Starting b at a to avoid duplicates, pythagorean theorem only works on right triangles 
        c_squared = a**2 + b**2  #getting c^2
        c = c_squared ** 0.5  #Taking the square root to find c
        
        if c % 1 == 0: #checking to see in c is an integer
            print(a, b, c)  #printing if c is an integer
