######################################################
# Lab 3-2
######################################################
# if-elif-else
a = 10
b = 20
c = 3

if a >= 100:
    b = a + 100
elif a >= 50:
    b = 200
elif a < 0:
    b = 100 -a

if (b**2 - 4*a*c) > 0:
    print('Two distint real roots')
elif (b**2 - 4*a*c) == 0:
    print('One real root')
else:
    print('No real root')

######################################################
# Compound Boolean Expressions
# you should able to answer the results by hand
a = 10
b = 20
c = 30

print((b > a) or (b > c))

print((b > a) and (b > c))

print((b <= (c - 10)) and not (a + b < c))

print(((b - c) < a) and (b % c == b) or (c//a <= a))

print(((b - c) == (a - b) ) or (b % c == b % a) or (c//a <= c//b))

######################################################
x = 42
if x >= 0 and x < 100:
    print()

if x % 3 == 0 and x % 7 == 0:
    print()

if x == 'y' or x == 'Y':
    print()

if (x % 5 == 0 and x < 200) or (x % 7 == 0 and x >= 40):
    print()

if x % 400 == 0 and x % 100 != 0:
    print()

######################################################
# Coding Lab: Seconds Conversion
######################################################

# enter seconds as input
seconds = int(input("Please enter a number of seconds: "))

# check three use cases
# better code has the order from the most restricted condition 
# to less restricted conditions
# use only one variable

if seconds >= 86400:
    print(seconds // 86400, " days")
elif seconds >= 3600:
    print(seconds // 3600, " hours")
elif seconds >= 60:
    print(seconds // 60, " minutes")

######################################################
# Coding Lab: Grade Conversions
######################################################
# ask input
# can either choose to use four lines of input() assignments
# or use some shortcut, make sure to convert into a numerical values
print("Please enter your grade of assignments, quizzes, midterm exams, and final exams, respectively:")
assignments, quizzes, midterm, final = int(input()), int(input()), int(input()), int(input())

# use formula to assign weights
grade = 0.3*assignments + 0.2*quizzes + 0.25*midterm + 0.25*final
print("Your final grade: ", grade)

# check grade's range
# method 1: using compound conditionals
if grade >= 90 and grade < 100:
    print('A')
elif grade >= 80 and grade < 90:
    print('B')
elif grade >= 70 and grade < 80:
    print('C')
elif grade >= 60 and grade < 70:
    print('D')
else:
    print('F')




# method 2: without using compound statements
# if grade >= 90:
#     print('A')
# # use multiple conditions with and operator
# elif grade >=80:
#     print('B')
# elif grade >=70:
#     print('C')
# elif grade >=60:
#     print('D')
# # the rest of case
# else:
#     print('F')