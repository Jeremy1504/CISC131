total = 0
tax_rate = 0.0875

number = float(input('Please Enter item price: (Enter -1 to quit): '))

while number != -1:
    total += number
    number = int(input('Please Enter a number (Enter -1 to quit): '))

print(f'Total: {total * (1+tax_rate):.2f}')
