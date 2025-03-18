#10demo.py by Metehan Teler

import math

print ('hello, again') #greeting

print (1.5e-2)

print (5 // 2) 
print (5 % 2)

print(math.pow (3,3))

a= 3 #side of triangle
b= 4 #side of triangle
c= math.sqrt(a**2 +b**2) #hypotenuse
print (c)
print (type(a), type(b), type(c)) #seeing what type of numerocal values
print (type(a), type(b), type(c), sep=', ', end='!\n') #creating custom spacer and ending

def meana(a, b, c): return ((a+b+c)/3)
print (meana(a, b, c)) #mean of the 3 sides

s = 'hello world'
print(s, type(s)) #storing hello world in string s, and seeing if its type is correct
if a == b:
    print('a equals b') #an if then statment that prints the string if a equals b
    
print(a,b) #we put this after the block so it is always reported

def is_even(x):
    if x % 2 == 0: return True #creating function if evenly divisible by checking if the remainder is 0
    return False
print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

#if elif else conditionals
if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b') #if elif else conditional statment which will print the first true statment

#Chaining boolean expressions
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

#Floating point warning
a = 0.3
b = 0.1 * 3
if   a < b: print('a < b') #this is what is printing even though its false because of finite percision with floating point values
elif a > b: print('a > b')
else:       print('a == b')
#manually checking percision
print(abs(a - b)) # 5.551115123125783e-17 -> this is the difference between a and b
if abs(a - b) < 1e-9: print('close enough')
if math.isclose(a, b): print('close enough') #this is a build in function that checks percision

#String Comparison
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a') #The letters are compared based on their ASCII values
"""#Mismatched type error
a = 1
s = 'G'
if a < s: print('a < s') #this results in an error because they are different types
#None Type error
def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4)) #since we never returned the function, the value becomes none
"""
#More practice 

def is_integer(x):
    if x % 1 == 0: return True #creating function if evenly divisible by checking if the remainder is 0
    return False
print(is_integer(2))
print(is_integer(2.1)) #checks if there is a remainder, whole numbers should not have a remainder when divded by 1

#molecular weight of a DNA letter
def is_dna(letter):
    if letter == 'A': print ('331')
    elif letter == 'C': print ('307')
    elif letter == 'G': print ('347')
    elif letter == 'T': print ('332')
    else: print('not a nucleotide')        #why is it printing 4 times?
print(is_dna('A'))
print(is_dna('T'))    

#Returning a complement DNA letter
def is_dcomp(letter):
    if letter == 'A': print ('T')
    elif letter == 'C': print ('G')
    elif letter == 'G': print ('C')
    elif letter == 'T': print ('A')
print(is_dcomp('A'))
print(is_dcomp('G'))