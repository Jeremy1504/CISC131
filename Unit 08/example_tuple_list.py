lst = [10, 20, 'Hello', [30, 40]]
print(lst)

tuples = tuple(lst)
print(tuples)

tuples[3][1] = 100

print(tuples)
print(lst)
