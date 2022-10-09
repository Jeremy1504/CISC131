# optional materials for advanced uers
#
# Use Recursive function
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        # recursive
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# test case
print(Fibonacci(3))
print(Fibonacci(10))

############################################################

# use recursive function
def factorial(n):
    # seed values
    if n == 0:
        return 1
    else:
        # recursive
        return n * factorial(n-1)

def sumUp(num):
    # Sum up a series of numbers

    # Running total
    total = 0

    for i in range(1, num+1):
        # call factorial function
        total += factorial(i)

    return total

def main():
    # input
    num = int(input('Enter a non-negative integer: '))
    
    # input validation
    while num < 0:
        num = int(input('Enter a non-negative integer: '))

    # print & call sumUp function
    print(sumUp(num))

main()
