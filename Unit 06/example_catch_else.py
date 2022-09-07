try:
    a = int(input('a: '))
    b = int(input('b: '))
    print(a/b)
except(ValueError, ZeroDivisionError) as err:
    print(err)
else:
    print('Done.')
