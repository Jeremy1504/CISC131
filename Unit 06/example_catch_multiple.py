try:
    a = int(input('a: '))
    b = int(input('b: '))
    print(a/b)
except(ValueError, ZeroDivisionError):
    print('Please Enter a valid value.')

print('Done')
