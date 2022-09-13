######################################################
# Lab 3-3
######################################################

# enter an integer as input
number = int(input("Please enter a number: "))

# check three use cases
#
if number % 5 == 0 and number % 3 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
######################################################

# ask user to enter weights
# make data conversion, use float()
weight = float(input('Please Enter the weight of a package (Pounds): '))

# check the range of weight
if weight > 0 and weight <= 2:
	rate = 1.5
elif weight > 2 and weight <= 6:
	rate = 3
elif weight > 6 and weight <= 10:
	rate = 4
elif weight > 10:
	rate = 4.75
else:
    print('Please Enter a Valid Number')

    
# alternative method
# if weight < 0:
#     # check input validation
# 	print('Should enter a positive value.')
# elif weight <= 2:
# 	rate = 1.5
# elif weight <= 6:
# 	rate = 3
# elif weight <= 10:
# 	rate = 4
# else:
# 	rate = 4.75

# calcualte the shipping charges
# and display the final results
print('The shipping charges ($): ', rate* weight)

######################################################
# ask user's input for three numbers
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))

# Proof by exhaustion
# if first > second
if a > b:
    # continue to check the first and the third
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c

# first <= second
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median number is", median)
