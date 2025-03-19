#Metehan 30demo.py unit follow along and practice problems
import math
import random

#Strings. Strings= text and can be assigned to variables
s = 'hello world'
print(s)

s1 = 'hey "dude"' #put different kinds of quotes in quotes to have quoted string
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do') #you can also put a backslash before a quote to tell python you are not using it as a delimiter
#\n makes a newline character \t is used to represent a horizontal tab

#string operators
#string comparison operators work like their numerical counterparts except they are compared by their ASCII values

#String functions

print(s.upper()) #this doesnt replace s with S, it creates an uppercase copy of S
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

#String Formatting

print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify

print('{} {:.3f}'.format('str.format', math.pi)) #older format, does same thing as 3 fixed digits

print('%s %.3f' % ('printf', math.pi)) 

#Indexes
seq = 'GAATTC'
print(seq[0], seq[1]) #0 is first letter, 1 is second

print(seq[-1]) #in negative indexes, you start counting backwards from the right

for nt in seq:
    print(nt, end='')
print() #iterating through characters in a string using a for loop, all in one line

for i in range(len(seq)):
    print(i, seq[i]) #iterating through letters by their indices using range(). len() sets the limit

#Slices
#slice is a subset of a container. Work a little like range in that they take an initial position and an end-before limit. 
s = 'ABCDEFGHIJ'
print(s[0:5]) #0 is initial and 5 is the end-before limit

print(s[0:8:2]) #when step size is ommited, it is assumed to be 1. Here it is 2.

print(s[0:5], s[:5])        # both ABCDE #you can ommit either the initial value which is 0, or the final value which is the length of the string
print(s[5:len(s)], s[5:])   # both FGHIJ 

print(s, s[::], s[::1], s[::-1]) #It may seem a little strange but s[0] is the same thing as s[0:1]. s[0] indexes a single element. s[0:1] is a slice that starts at the zero-th element and ends before the first.s is also equivalent to s[0:len(s)] and s[::], which explicitly or implicitly set the bounds of the slice to the whole string. While it is not very surprising that s[::1] is also the same thing, your should definitely take a long look at s[::-1].

dna = 'ATGCTGTAA' #slicing string into codons
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(i, codon) 

#Tuples
#Let's take another look at tuples. A tuple is container that holds multiple values. Tuples are generally constructed with comma-separated values (usually in parentheses).
tax = ('Homo', 'sapiens', 9606)  # construct tuple
print(tax)                       # note the parentheses in the output
"""
s[0] = 'C'
tax[0] = 'human' #tuples and strings are imutable, these lines generate type errors
"""
#tuples can be indexed and sliced like strings
print(tax[0])      # index
print(tax[::-1])   # slice

#enumerate() and zip()
#enumerate ()
nts = 'ACGT'
for i in range(len(nts)): #When stepping through containers, it's often useful to have both indices and values. One way to do this is with the range() function.
    print(i, nts[i])

for i, nt in enumerate(nts):
    print(i, nt) #A tidier alternative is to have enumerate() provide you a tuple containing the index and value in separate named variables.
#zip()
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i]) #When stepping through two containers in parallel, you can use range() to simultaneously index separate containers.

for nt, name in zip(nts, names):
    print(nt, name) #The tidier solution uses zip() to retrieve an element from each container and return them to you in a tuple.

for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name) #You can even enumerate the zip as shown below. Here, you have to unpack the tuples in series using additional parentheses.

#Lists

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts) #Lists are similar to tuples except they are constructed with square brackets and their contents are mutable.

nts.append('C')
print(nts) #Elements can be added to the end of a list with list.append(). Like strings, most operations on lists use method syntax.

last = nts.pop()
print(last) #Remove elements from the end of a list with list.pop().

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts) #Lists are sorted with list.sort(). Note that all of the elements in the list must have similar types. You can sort a mixture of ints and floats, but you cannot mix them with strings.

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides) #If you make a new variable to an existing list, it is not a copy, but another name for the same list. In the example below, nucleotides is modified and the modifications also occur in nts because both variable names correspond to the same underlying data.
#To make a copy, use list.copy(). This is a "shallow" copy, meaning that multi-dimensional lists and other complex data structures are not fully copied. We don't make deep copies in this class. We also haven't talked about multiple dimensions yet.

#list()

items = list() #The list() function without arguments creates empty lists.
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff) #You can also create empty lists with empty square brackets.

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas) #The list() function coerces other "iterables" into lists. For example, it can convert a string into a list of letters.

#split() and join()

text = 'good day          to you'
words = text.split()
print(words) #The str.split() method splits strings into lists of strings. This is useful for segmenting words. By default, the delimiter is any number of spaces.

line = '1.41,2.72,3.14'
print(line.split(',')) #For TSV or CSV data, split on \t or comma

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s) #Lists can be turned into strings by joining them with a delimiter. The delimiter can be nothing. Here, the list is an argument to a method owned by the delimiter string (which can be empty).

#Searching
#To search for items in containers, you can use in, find(), and index(). The keyword in reads particularly well in conditional statements.
if 'A' in alph: print('yay')
if 'a' in alph: print('no')
"""
print('index G?', alph.index('G'))
print('index Z?', alph.index('Z')) #The index() method returns the index of the first element it finds. If it can't find a matching item, the function throws an error.
"""

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z')) #The find() method returns the index of the first element it finds or a -1 if it can't be found. This very useful behavior only works for strings, and not tuples or lists.

"""
if you are searching a list or tuple, and you don't know if the element is in the list, first use in.
# don't put this in your 30demo.py, it's just an example
if thing in list: idx = list.index(thing)
"""

#Practice Problems

#minimum()
def minimum(vals):
    mini = vals[0] #assigning first number as the minimum
    for val in vals[1:]: #Iterating through remaining numbers
        if val < mini: mini = val #Updating minimum if smaller value is found
    return mini
numbers = [8, 6, 6, 4, 3, 1]
print(minimum(numbers))

#minmax()
def minmax(vals):
    mini = vals[0] #assigning minimum to first value
    maxi = vals[0] #assigning maximum to first value
    for val in vals: #Iterating through remaining numbers
        if val < mini: mini = val #updating the minimum if a smaller value is found
        if val > maxi: maxi = val #updating the maximum if a larger value is foubd
    return mini, maxi #returning both values as a tuple.

print(minmax(numbers))

#mean()
def mean(vals):
    total = 0 #creating a variable for the total
    for val in vals: total += val #Iterating through each value in the list and summing them
    return total / len(vals) #dividing total value over number of items on the list
print(mean(numbers))

#entropy()
def entropy(probs):
    h = 0 #creating a variable for entropy to sum later
    for p in probs:
        if p > 0:
            h -= p * math.log2(p)
    return h
print(entropy([0.2, 0.3, 0.5]))

#dkl()
#P and Q are distributions, p and q are individual values. 
def dkl(P, Q):
    d = 0
    for p, q in zip(P, Q):
        if p > 0 and q > 0:
            d += p * math.log2(p/q)
    return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))

#Command Line Data
#sys.argv

import sys
print(sys.argv) #The variable sys.argv is the complete list of words on the command line (argv is short for argument vector). sys.argv[0] is the name of your program. sys.argv[1] is the first argument, if there is one.
#sys.argv is a list

#Converting Types
#Data that you read from the command line and from files (see next unit) are in the form of strings. You have to convert text representations of numbers to ints and floats before you can do math with them. The int() and float() functions do that.

i = int('42')
x = float('0.61803')
print(i * x)

"""
x = float('hello') #you get a cannot convert string to quote error
"""
#There are several ways to interact with error conditions in Python. We do not go over assert, try, except, or raise in MCB185. If you run into an error and want to provide a custom message, use sys.exit().