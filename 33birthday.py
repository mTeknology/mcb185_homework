#Metehan 33birthday.py homework

import random
import sys

students = int(sys.argv[1]) #Order you write in command line is important
days = int(sys.argv[2]) 
trials = int(sys.argv[3]) 

sharedbday = 0 #creating a variable to store shared bdays

for trial in range(trials):
    birthdays = [] #Creating a variable to store birthdays
    duplicate = False #flag to track duplicates

    for kid in range(students):
        bday = random.randint(0, days - 1) #random birthday generator
        if bday in birthdays:  # Check if this birthday is already in the list
            duplicate = True
            break  # Short-circuit ones a duplicate is found
        birthdays.append(bday) #If we do not trigger the short circuit, we add the day to the list.

    if duplicate:
        sharedbday += 1

probability = sharedbday / trials
print("Probability of a Shared Birthday ", probability)
