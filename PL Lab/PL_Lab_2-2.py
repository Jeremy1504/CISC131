# use input message to ask user's input
# convert input string into float data type
food_charge = float(input('Please enter the charge for the food: '))

# given information
# tips and tax
tips = 0.18
sales_tax = 0.07

# use formula to calculate total charge
total_amount = food_charge * (1+tips+sales_tax)

# print them on screen
print(total_amount)

###############################################################################

# use input message to ask user's input
# convert input string into float data type
temp_celsius = float(input('Please enter a temperature in Celsius: '))

# use formula
temp_fahr = 9/5*temp_celsius+32

# print result on screen
print(temp_fahr)

###############################################################################
# ask user's input
# no loop, list, .split() yet
# will cover those later
score_1 = int(input('Please Enter your first test score: '))
score_2 = int(input('Please Enter your second test score: '))
score_3 = int(input('Please Enter your third test score: '))
score_4 = int(input('Please Enter your fourth test score: '))

# simple math to calculate average
average = (score_1 + score_2 + score_3 + score_4)/4

# print result
print('Your average score is ', average)

###############################################################################

# assign variables
future_value = 120000
annual_interest_rate = 0.04
number_of_years = 20

# use the given formula
# make sure to use pairs of parentheses
present_value = future_value/((1+annual_interest_rate)**number_of_years)

# print with 2 decimal point format
print(f'The amount of deposit today is {present_value:.2f}')
