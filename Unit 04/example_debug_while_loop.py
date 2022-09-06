total = 0
n = 1

print('while loop: ')

while (n < 10):
	# add print i th iteration
	print(str(n) +' iteration: ')
	total += n
	# print total values after increment
	print('total =', total)
	n += 1
	# print n after increment update
	print('n =', n)
	# print a new empty line
	print()
	
print(total)