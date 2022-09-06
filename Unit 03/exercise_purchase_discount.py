number = int(input('Please Enter the number of packages purchased: '))
price = 99

# good habit to check invalid inputs
if number < 0:
	print('error')
	exit() # interrupt program

elif number < 10:
	discount = 0
elif number < 20:
	discount = 0.1
elif number < 50:
	discount = 0.2
elif number < 100:
	discount = 0.3
else:
	discount = 0.4

print('Discount: ', discount*100, '%')
price_after_discount = price*(1-discount)*number
print(f'Total purchase: ${price_after_discount:.2f}') # use python 3 format
