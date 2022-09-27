# set accumulator to 0
total = 0

# repeat 5 times
for i in range (1, 6):
	# ask a number from keyboard and store as a float number
	num = float(input('Enter a number: '))
	# add this number to the accumulator
	total = total + num

# print final accumulator's value
print(total)
