lst = [10, 11, 12, 13, 14, 15]

# print every item in a list
for num in lst:
    print(num, end = ' ') # print each number and separate by a white space

print()
for num in lst:
    if num % 2 == 0: # add a condtional statment to filter even numbers
        print(num, end = ' ')
