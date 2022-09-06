weight = float(input('Please Enter the weight of a package (Pound): '))

if weight < 0:
	print('error')
	exit()
elif weight <= 2:
	rate = 1.5
elif weight <= 6:
	rate = 3
elif weight <= 10:
	rate = 4
else:
	rate = 4.75

print('The shipping charges ($): ', rate* weight)

