n = int(input('Enter a number: '))

while n > 0:
	if n % 2 == 0:
		print(n, 'is an even number')
	else:
		print(n, 'is an odd number')
	n = n - 1
