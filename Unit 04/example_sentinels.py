sum_num = 0
count = 0

number = int(input('Please Enter a number (Enter a negative number to quit): '))

while number >=0:
    sum_num += number
    count += 1
    number = int(input('Please Enter a number (Enter a negative number to quit): '))

print(f'Sum: {sum_num}, Average: {sum_num/count}')
