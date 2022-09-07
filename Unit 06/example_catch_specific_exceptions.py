try:
    a = int(input('a: '))
    b = int(input('b: '))
    print(a/b)
except ZeroDivisionError:
    print('Cannot divide with zero.')
except ValueError:
    print('Entered value is wrong')
