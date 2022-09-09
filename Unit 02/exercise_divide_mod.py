num_days = 300

# floor division to find quotient
weeks = num_days // 7
# mod division to find the remainder
days_remain = num_days % 7

# print final results
print('Week: ', weeks)
print('Remaining Days : ', days_remain)