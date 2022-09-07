lst = ['Hello' , 'World', 'Python']

# Method 1
print(''.join(lst))

# Method 2
s = ''
for i in lst:
    s += i
print(s)

# Method 3
s = ''.join([str(x) for x in lst])
print(s)

# Method 4
s = ''.join(map(str, lst))
print(s)
