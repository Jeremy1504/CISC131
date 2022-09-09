myList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

print(myList[0])
print(myList[2])
print(myList[7])

# use try except to catch IndexError
try:
    print(myList[12])
    print(myList[15])
except IndexError:
    print('Index out of range.')
print(myList[-1])

# use try except to catch IndexError
try:
    print(myList[-13])
except IndexError:
    print('Index out of range.')
