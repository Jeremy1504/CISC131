# string is immutable
string = 'Hello'
string[1] = '20' # error
print(string)


# list is mutable
lst = [10, 'Hello', 30]
lst[1] = 20

print(lst)
del lst[0]
print(lst)
