month = int(input('Please enter a month using an integer: '))

# w/o using other data structure
if month < 1 or month > 12:
    print('error')
    exit()
elif month == 2:
    print(28)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
else:
    print(31)