number = int(input('Please Enter a non-zero number (Enter 0 to end): '))

total = 0

while number!=0:
    if number > 0:
        total += number
    else:
        total -= number
        
    number = int(input('Please Enter a non-zero number (Enter 0 to end): '))


print(f'Sum: {total}')


