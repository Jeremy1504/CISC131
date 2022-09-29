print('------ Lab 4-1 Coding------')

# loop from 1 to 5
for i in range(1, 6):
    # python support multiple with text string
    print('*' * i)

# loop from 4 to 1
# be careful about the boundary
for i in range (4, 0, -1):
    print('*' * i)

###########################################################################


numbers = [12, 20, 35, 75, 150, 180, 145, 200,  256, 525, 50, 300, 175]

# use a for loop to iterate list of numbers
for i in numbers:
# use conditional statement to check value
    if i % 5 ==0 and i >= 150 and i < 200:
        # if the number satisfy the condition, then print the value
        print(i)

###########################################################################
