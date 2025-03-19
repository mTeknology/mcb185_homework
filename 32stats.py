#Metehan 32stats.py 
import math
import sys




def minmax(vals):
    mini = vals[0] #assigning minimum to first value
    maxi = vals[0] #assigning maximum to first value
    for val in vals: #Iterating through remaining numbers
        if val < mini: mini = val #updating the minimum if a smaller value is found
        if val > maxi: maxi = val #updating the maximum if a larger value is foubd
    return mini, maxi #returning both values as a tuple.
    
def mean(vals):
    total = 0 #creating a variable for the total
    for val in vals: total += val #Iterating through each value in the list and summing them
    return total / len(vals) #dividing total value over number of items on the list

def stdev(vals, mean_value):
    sqdiff = 0
    for val in vals:
        sqdiff += (val - mean_value) ** 2
    return math.sqrt(sqdiff / len(vals))

def median(vals):
    vals.sort()  # Sorting the list)
    n = len(vals) # Assigning n as the length of the string
    if n % 2 == 1:  # If there is a odd number of values
        return vals[n // 2] #report the middle one
    else:  #Taking the median of an even number of values
        med1 = vals[n // 2 - 1]
        med2 = vals[n // 2]
        return (med1 + med2) / 2

numbers = [float(arg) for arg in sys.argv[1:]]
mini, maxi = minmax(numbers) 
mean_value = mean(numbers)
st_dev = stdev(numbers, mean_value)
median_value = median(numbers)

print('Number of Values ', len(numbers))
print('Minimum Value ', mini)
print('Maximum Value ', maxi)
print('Mean ', mean_value)
print('Standard Deviation ', st_dev)
print('Median ', median_value)