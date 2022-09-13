######################################################
# Lab 3-1
######################################################
a = 10,
b = 20
c = 3
number = 101
password = 'hello'

if a >= 5:
    print(2**a)
else:
    print(a**2)

if password == 'Pa$$w0rd':
    print('Password Correct')
else:
    print('Password Incorrect')

if a >= 100:
    b = a + 100
elif a >= 50:
    b = 200
elif a < 0:
    b = 100 -a

if number % 2 == 0:
    print(number, ' is even')
else:
    print(number, ' is odd')

if (b**2 - 4*a*c) > 0:
    print('Two distint real roots')
elif (b**2 - 4*a*c) == 0:
    print('One real root')
else:
    print('No real root')

######################################################
# Coding Lab: Seconds Conversion
######################################################

# enter seconds as input
seconds = int(input("Please enter a number of seconds: "))

# check three use cases
# better code has the order from the most restricted condition 
# to less restricted conditions

if seconds >= 86400:
    print(seconds // 86400, " days")
elif seconds >= 3600:
    print(seconds // 3600, " hours")
elif seconds >= 60:
    print(seconds // 60, " minutes")


