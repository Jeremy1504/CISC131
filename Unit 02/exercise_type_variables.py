a = 100
print(type(a))
print(type(float(a)))

b = str(a)
print(type(b))

# bug
print(100+b)

# fixed using int()
print(100+int(b))
