my_string = "Hello World!"
print(my_string[0])
print(my_string[6])

print(my_string[-3])
print(my_string[-11])

string = "Hello World!"
print(string[0])
print(string[5])
print(string[11])

try:
    print(string[12])
except IndexError:
    print('Index out of range')

print(string[-1])
print(string[-5])

try:
    print(string[-15])
except IndexError:
    print('Index out of range')