a = 100
# use type function to check data types of a variable
print(type(a))
# cast float() to convert a variable to a float data type
print(type(float(a)))

# cast str() to convert a variable to a string data type
b = str(a)
print(type(b))

# bug, not the same data types
# the addition operation won't work
print(100+b)

# fixed by using int() or float()
print(100+int(b))
