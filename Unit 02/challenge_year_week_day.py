days = int(input('Please Enter the Days: '))

years = days // 365
weeks = days % 365 // 7
days_remain = days % 365 % 7

print('Year: ', years)
print('Week: ', weeks)
print('Year: ', days_remain)
