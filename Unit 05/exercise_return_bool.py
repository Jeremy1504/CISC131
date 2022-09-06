def is_even(number):
    if number % 2 == 0:
        status = True
    else:
        status = False
    return status

num = int(eval(input('Enter a number: ')))

if is_even(num):
   print('It is an even number')
else: 
   print('It is an odd number')
