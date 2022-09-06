# if-else
num = int(input('Enter a number: '))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print('Not a Prime')
            exit()

    print('Prime')
else:
    print('Not a Prime')


# alternatively, use boolean variable and break
num = int(input('Enter a number: '))

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

# check if flag is True
if flag:
    print(num, 'Prime')
else:
    print(num, 'Not a Prime')

