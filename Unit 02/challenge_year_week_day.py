# ask user to enter the value of days
# make sure convert it to an integer data type
days = int(input('Please Enter the Days: '))

# floor division
years = days // 365

# how many days left after converted to years
weeks = days % 365 // 7

# how many days left after converted to years and weeks
days_remain = days % 365 % 7

# print the final results
print('Year: ', years)
print('Week: ', weeks)
print('Day: ', days_remain)
