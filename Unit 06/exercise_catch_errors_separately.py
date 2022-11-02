my_string = 'Hello World'

try:
    print(my_string)

    # num = int(my_string)
    # print(my_string + 100)
    # num = 1/0
    print(total)
    
except ValueError:
    print('Value Error')

except TypeError:
    print('Type Error')

except ZeroDivisionError:
    print('ZeroDivision found')

except:
    # handle all other exceptions
    print('Some error happened')

print('Done')


