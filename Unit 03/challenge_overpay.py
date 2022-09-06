hours = float(input('Please Enter the hours: '))

if hours > 40:
	regular_pay = 30 * 40
	overtime_pay = 30 * 1.5 * (hours - 40)
	print('The Gross Pay is ', regular_pay+overtime_pay)
else:
	regular_pay = 30 * hours
	print('The Gross Pay is ', regular_pay)