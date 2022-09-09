test_lst = ['A', 10, 20]

# method 1: loop
def reverseList(lst):
    rev_lst = []
    for i in range(len(lst)-1,-1,-1):
        rev_lst.append(lst[i])
    return rev_lst

print(reverseList(test_lst))



test_lst = ['A', 10, 20]

# method 2: index slicing
def reverseList_slice(lst):
    return lst[::-1]

print(reverseList_slice(test_lst))

# method 3: 
# reverse() method 
# with placement
test_lst = ['A', 10, 20]
test_lst.reverse()
print(test_lst)


# method 4
# list comprehension 
# with reversed() method

test_lst = ['A', 10, 20]
def reverseListComp(lst):
    return [item for item in reversed(lst)]

print(reverseListComp(test_lst))