#Metehan Unit 2 follow along
import random

t = 1, 2  # this is a tuple, a collecton of values seperated by a comma
print(t)
print(type(t))

person = 'Steve', 21, 57891.50 # name, age, yearly income, tuples can hold multiple types
print(person)

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

print(midpoint(1, 2, 3, 4)) #calls midpoint and prints
m = midpoint(1, 2, 3, 4) #assigns m to the return value above, m is a tuple
mx, my = midpoint(1, 2, 3, 4) #unpacks the tuple, the caller knows that the function returns two values and provides 2 seperate named variables
print(mx, my) # prints

print(m[0], m[1]) # Each item in a touple gets a numeric index starting at 0. This replaces line two and gets the same outcome

#Iteration (looping)
#While is the simples loop. This word is followed by an expression that is true or false
#while <boolean expression is True>:
#    do_something
"""
while True:
    print('hello') #started printing hello infinetely 
"""
i = 0 #i stores an integer
while True:
    i = i + 1 #each time it loops, the integer increases by 1
    print('hey', i)
    if i == 3: break #break a loop with break, which happens here when i reaches 3.

i = 0
while i < 3:
    i = i + 1
    print('hey', i) #a better way to break is to provide a condition where boolean expression is no longer true

i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i) #the loop can start anywhere and can skip 

for i in range(1, 10, 3): #for is mostly use (range is a function generates integers given an initial value (1), an end-before limit (10), and an increment (3).
    print(i) 

for i in range(0, 5): #The default increment is 1, so you do not have to include the last digit
    print(i)

for i in range(5): #it also default starts at 0, so you can skip that too.
    print(i)

for i in range(5): print(i)
for i in range(0, 5): print(i)
for i in range(0, 5, 1): print(i) #these all do the same thing

for i in range(4, -1, -1): print(i) #this counts backwards starting at 4

#for item in container
basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing) #basket is a thuple. The code steps through the items one at a time. 

for i in range(len(basket)):
    print(basket[i]) #you could use I and a numeric index. len() returns the number of items in the basket. When run it actually just listed the items again

#Nesting
#Conditionals can be inside loops. Loops can be inside conditionals. Loops can be inside of other loops. More abstractly, a code block may contain other code blocks. Here's a simple loop that iterates over some numbers and reports which ones are even and odd. If you recall that range() automatically starts at 0 and ends before it reaches the limit, you will not be surprised that the loop goes from 0 to 6 inclusive.
for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd') #Lists all numbers 0-6 and says if it is even or odd

#Practice problems after fizzbuzz
#Write a function that calculates the triangular number. This is the sum of numbers from 1 to n.
def triangular(n):
    tri = 0 #Variable that holds the sum
    for i in range(n+1):
        tri = tri + i #adds current value of loop variable in each iteration
    return tri

#Write a function that calculates the factorial of a number.
def factorial(n):
    if n == 0: return 1 #since factorial 0 is one, we use a conditional for this special case
    fac = 1 #we have to initialize at 1, if we started at 0 we'd always get 0 when multiplying
    for i in range(1, n + 1):
        fac = fac * i
    return fac
"""
#Write a function that computes the Poisson probability of k events occurring with an expectation of n: n^k e^-n / k!
def poisson(n, k):
    return n**k * math.e**-n / factorial(k

#Write a function that solves "n choose k": n! / k!(n - k)!
def nchoosek(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k)) #since we defined factorial earlier, we can reuse it


#Write a function that estimates Euler's number: e (2.71828...). This can be computed as the infinite sum of 1/n!. Choose a finite number of iterations.
def euler(limit): #simillar to triangular because it sums up a bunch of numbers
    e = 0
    for n in range(limit):
        e = e + 1 / factorial(n)
    return e

#Write a function to determine if a number is prime.
def is_prime(n): # this is a short circuiting algorithm that returns false as soon as it finds any factor smaller than it self. If it cant it returns true
    for den in range(2, n//2 +1):
        if n % den == 0: return False
    return True

#Write a function that estimates Pi (3.14159...) using the Nilakantha series. Again, choose a finite limit. Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...
def nilakantha(limit): #We must create a loop that goes back and forth between addition and subtraction
    pi = 3
    for i in range(1, limit+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d
        else:          pi = pi + 4 / d
    return pi

#Random Numbers
#important for random expectation, background model, or null hypothesis. Must use: import random  In ordor to call these functions
import random

for i in range(5):
    print(random.random()) #simplest number that produces a number 0 <= X < 1

for i in range(3):
    print(random.randint(1, 6)) #random.randint generates a random number between two inclusive points. This code simulates rolling a 6 sided die 3 times.

#Numbers arent truly random, they are generated deterministically given a starting seed. All random number problems can be repeated exactly the same repeatedly. This is useful for debugging
"""
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random()) #each random.seed() resets the random number generator so that subsequent calls to random.random are repeated


#Compound Assignment
#compound assignment operators do the math and update the variable at the same time.
#replaces x = x + 1 with x += 1   there is also -= and *=

#More practice
#Monty Pi-thon
"""
#import random (already done in this file)
inside = 0 #variable for points inside the circle
total = 0 #variable for total points
while True: #endless loop
    x = random.random()
    y = random.random()
    distance = (x ** 2 + y **2) **.5 #distance from origin
    if distance < 1: #checks if point is within circle
        inside += 1
    total += 1 #Incrementing points
    pi_estimate = 4 * (inside/ total) #estimates pi
    print(pi_estimate)
"""
#D and D Stats

def roll_3d6():
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

def roll_3d6r1():
    d1 = random.randint(1, 6) #creating variables for each roll
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6) #rolling 3 times
    if d1 == 1: d1 = random.randint(1, 6)
    if d2 == 1: d2 = random.randint(1, 6)
    if d3 == 1: d3 = random.randint(1, 6) #rerolling ones

    return d1 + d2 + d3

def roll_3d6x2():
    d1a, d1b = random.randint(1, 6), random.randint(1, 6)
    d2a, d2b = random.randint(1, 6), random.randint(1, 6)
    d3a, d3b = random.randint(1, 6), random.randint(1, 6) #rolling 2 pairs 3 times

    if d1b > d1a: d1a = d1b
    if d2b > d2a: d2a = d2b
    if d3b > d3a: d3a = d3b #taking the highest of the 3 pairs
    return d1a + d2a + d3a

def roll_4d6d1():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6) #rolling 4 times
    
    smallest = d1 #creating a variable for the smallest roll
    if d2 < smallest: smallest = d2
    if d3 < smallest: smallest = d3
    if d4 < smallest: smallest = d4 #updating smallest by comparing rolls
    
    return (d1 + d2 + d3 + d4) - smallest  # Subtract the smallest value

print("3D6:      ", roll_3d6())
print("3D6r1:    ", roll_3d6r1())
print("3D6x2:    ", roll_3d6x2())
print("4D6d1:    ", roll_4d6d1()) #testing
