print('------ Lab 4-3 Coding------')

# counter
count = 0

# loop: ask user to enter 5 times
for i in range(1, 6):
    user_input = input('Please Enter a word: ')
    # for each words, loop through every character
    for character in user_input:
        # if every character is 'a'
        if character == 'a':
            # if so, count number +1
            count += 1
print(count)

###########################################################################

# input
n = int(input("Please enter a positive integer: "))

# while loop to keep checking valid input
while (n <= 0):
    n = int(input("Please re-enter a positive integer: "))

# total variable initialization
total = 0

# loop from 1 to n
for i in range(1, n + 1):
    # sum up values
    total += i * (i + 1)

print("Total is ", total)

###########################################################################

# initialization 
# how many numbers entered, 
# and total value
count = 0
sum_up = 0

# keep asking user to enter values
while True:
    n = int(input("Please enter a series of natural numbers integer (Enter 0 when finished): "))
    
    # only break loop when enter target exit value
    if n == 0:
        break
    # sum up values  
    sum_up += n
    # count how many values entered
    count +=  1

# average
average = sum_up / count

# print("The sum of this series is %d. The average of this series is %.2f." % (sum_up, average))

# use python 3 format
print(f'The sum of this series is {sum_up}. The average of this series is {average:.2f}')


###########################################################################
# for() loop
#
# print multiplication table
# first_number * second_number
# first number is the row
# second number is column
# decrement by 1

n = 5

# outer loop: the first number, loop from n to 1
for i in range(n, 0, -1):
    
    # inner loop: the second number, loop from i to 1
    for j in range(i, 0, -1):
        # print multiplication table
        # print('{} x {} = {}\t'.format(i, j, i*j), end = '')
        # using python 3 format (optional)
        print(f'{i} x {j} = {i*j}\t', end = '')
    print()

###########################################################################
#
# while loop()

m = 5

# outer loop: the first number (row)
while (m >= 1):
    n = m
    # inner loop: the second number (column)
    while (n >= 1):
        # print table
        print(f'{m} x {n} = {n*m}\t', end = '')
        # decrement column by 1
        n -= 1
    # print the next line
    print()
    # decrement row by 1
    m -= 1