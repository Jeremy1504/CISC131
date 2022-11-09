sequence = (10, 20, 'Hello', [30, 40])
print(sequence)
print(type(sequence))

try:
    sequence[2] = 100
except TypeError as err: # catch TypeError
    print(err)

sequence = list(sequence)
print(sequence)
print(type(sequence))

sequence[2] = 100 # no error

sequence = tuple(sequence)
print(sequence)
print(type(sequence))
