#Metehan, Fizzbuzz assignment

for i in range(1, 101): #uses 101 because it is inclusive
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz') #divisible by 3 and 5 (remainder is 0)
    elif i % 3 == 0:
        print('Fizz') #divisible by 3
    elif i % 5 == 0:
        print('Buzz') #divisible by 5
    else:
        print(i) #prints the numbers 