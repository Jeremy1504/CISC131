n = 7

# descending range
factorial = 1
for i in range(n, 0, -1):
    factorial = factorial * i

print(factorial)

# using ascending range
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i

print(factorial)
