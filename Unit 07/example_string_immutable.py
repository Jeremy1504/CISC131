b = 'World'
try:
    b[2] = 'A'
except TypeError as err:
    print(err)

