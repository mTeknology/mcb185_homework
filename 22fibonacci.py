#Metehan 22fibonaci problem

a, b = 0, 1  #initializeing the first two values and assigning them to variables

print(a)
print(b)

for i in range(8):  #generating the next 8 values using a loop
    next_value = a + b  #Fibonacci: adding the previous 2 values together to get the next one
    print(next_value)
    a, b = b, next_value  #Updating variables, a becomes b and b becomes new value
