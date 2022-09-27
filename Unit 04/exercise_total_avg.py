# how many numbers to input
n = 3

# initalize coutner variables
total = 0
count = 0

# loop multiple times
for i in range(1, n+1):
    # ask user to enter a value and store it as float data type
    value = float(input('Please enter a number: '))

    # counter increase by 1
    count += 1
    # total amount increase by the value
    total += value

# display the final counter variable's value
print('Total : ', total)
print('Average : ', total/count)
