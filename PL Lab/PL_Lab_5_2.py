# import math library
import math

# define function
def surface_sphere(r):
    # use TSA formula
    return 4*math.pi*(r**2)

# define function
def surface_cylinder(r, h):
    # use TSA formula
    return 2*math.pi*(r**2)+2*math.pi*r*h

# ask user to enter r and h
# convert the input into float data type
r = float(input('Enter radius (r): '))
h = float(input('Enter the height (h): '))

# print calculation results
# call defined functions and pass the arguments
print(f'TSA of a sphere: {surface_sphere(r):.2f}')
print(f'TSA of a cylinder: {surface_cylinder(r, h):.2f}')

#########################################################

def findMax(lst):
    # initialize with a really small number
    largest = -99999999

    # iterate each number in a list
    for i in lst:
        # if the current number is larger than the accumulator
        if i > largest:
            # then, set the accumulator as the current number
            largest = i
    
    # after loop, return the value of largest
    return largest


lst = [10, 20, -30, 17, 25, 6, -29]
print(findMax(lst)) # call with argument

#########################################################
import random

def avgNum(n):
    # input validation
    if n <= 0:
        print('n should be a positive integer.')
        # use exit()
        # or use return 0
        return 0
    else:
        total = 0

        # generate numbers for n times
        for i in range(n):
            # accumulator
            total += random.randint(1, n)
        return total/n

print(avgNum(20))
print(avgNum(100))