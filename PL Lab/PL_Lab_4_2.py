print('------ Lab 4-2 Coding------')

tuition = 9000
growth_rate = 0.035

n = 5

for i in range(1, n + 1):
    projected_tuition = tuition * (1+growth_rate) ** (i)
    print(i, round(projected_tuition, 2))
    # python 3 format
    # print(f'{i}, {projected_tuition:.2f}')

###########################################################################

# input
n = int(input("Please enter a nonnegative integer: "))

# input validation, simple check
if n <= 0:
    print('Error: invalid input.')
    exit()

# initialize total variable
total = 0

# loop from 1 to n
for i in range(1, n+1):
    # debug print
    # print(1/i)
    # accumulate total number
    total = total + 1/i

# format with 2 decimal
print(f'Sum is {total:.2f}')

###########################################################################

# input
number = int(input("Please enter a positive integer (n): "))

# valid input range
if number > 0:

    # initialize total variable that will hold the sum up of all proper divisor
    sum_up = 0
    
    # loop from 1 to n - 1
    for i in range(1, number):
        # A proper divisor of a natural number is the divisor that is strictly less than the number 
        if number % i == 0:
            print(i) # debug use: show proper divisor
            sum_up +=  i
    
    # check perfect number
    # whether this number is equal to the sum up of divisor
    if sum_up == number:
        print(number, " is a perfect number.")
    else:
        print(number, " is NOT a perfect number.")

# invalid case message
else:
    print("Please enter a positive integer.")

###########################################################################

# stick to factorial formula

n = int(input("Please enter a nonnegative integer: "))

# starting from the boundary case
if n == 0:
    factorial = 1

elif n > 0:
    # initialize a num to store factorial
    factorial = n
    # loop from n-1 to 1
    for i in range(n-1, 0, -1):
        # use formula 
        factorial = factorial * i
        
print(factorial)

###########################################################################

# another method, stick to factorial formula, while() loop
number = int(input("Please enter a nonnegative integer: "))

if number >= 0:
    factorial = 1
    while (number > 1):
        factorial = factorial * number
        number = number -1
    print(factorial)