#################################################################
# Lab 7 - Part I Basics and Methods
######################
# 1
# regular method: append item in a list
def printList():
    lst = []
    for i in range(1, 21):
        lst.append(i**2)
    print(lst[5:])


printList()

# 2
# use index() to locate index position
# list is mutable in Python

def replaceList(lst, num):
    index = lst.index(num)
    lst[index] = 100

    return lst


test_lst = [5, 10, 15, 20, 25, 30, 20, 10]
print(replaceList(test_lst, 10))


# 3
# regular method: loop
def removeDivNum(lst):
    removed_lst = []
    for num in lst:
        if num % 5 != 0 and num % 7 != 0:
            removed_lst.append(num)
    return removed_lst

# alternative method: list comprehension
def removeDivNum(lst):
    return [x for x in lst if x % 5 != 0 and x % 7 != 0]

test_lst = [12, 24, 35, 70, 88, 120, 155]
print(removeDivNum(test_lst))

#################################################################
# Lab 7 - Part II 2D-lists
######################
# 4
# use sorted() method + list comprehension
def sortLst(lst):
    return [sorted(x) for x in lst]


test_list = [[70, 20, 30], [90, 100, 30], [90, 70, 60]]

print(sortLst(test_list))
# check original list
print(test_list)

# 5
# several sub-functions
def checkMatrix(lst):
    # modularization with several functions
    import math

    def isPrime(n):
        # boundary value check
        if (n <= 1):
            return False
        # more efficient to check up to root(n)
        for i in range(2, (int)(math.sqrt(n)) + 1):
            if (n % i == 0):
                return False

        return True

    # function to find the sum of the given matrix
    def takeSum(matrix):

        total = 0
        # the length of row
        for i in range(0, len(matrix)):
            # the length of each row
            for j in range(0, len(matrix[i])):
                total += matrix[i][j]

        return total

    # call our functions
    num = takeSum(lst)
    print(num)  # double check sum values
    if isPrime(num):
        print("YES")
    else:
        print("NO")

# test case
test_matrix = [[1, 25, 3, 4, 2],
               [10, 11, 25, -9, 34],
               [-10, 24, 29, 22, 12],
               [1, -20, 3, 3, 9]]

# 179 is a prime number, should return "YES"
checkMatrix(test_matrix)
