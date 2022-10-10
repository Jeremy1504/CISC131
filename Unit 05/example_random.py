import random

num = random.random() # random generate a number [0, 1]
print(num)

number = random.randint(0, 10) # random generate a number [0, 10]
print(number)

for i in range(0, 10): # repeat 10 times
    number = random.randint(1, 100) # random generate a number [1, 100]
    print(number, end = ',') # split each number with a comma
