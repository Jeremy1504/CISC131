month = int(input('Please enter a month using an integer: '))

if month < 1 or month > 12:
    print('error')
    exit()
elif month == 2:
    print(28)
# use list data structure
elif month in [4, 6, 9, 11]:
    print(30)
else:
    print(31)