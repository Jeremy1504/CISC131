first_name = input("Enter the first name: ")
second_name = input("Enter the second name: ")
third_name = input("Enter the third name: ")

# first_name is less than second name
if first_name <= second_name:
	if third_name <= first_name:
		print(third_name, first_name, second_name)
	elif third_name >= second_name:
		print(first_name, second_name, third_name)
	else:
		print(first_name, third_name, second_name)

# first_name is larger than second_name
else:
	if third_name >= first_name:
		print(second_name, first_name, third_name)
	elif third_name <= second_name:
		print(third_name, second_name, first_name)
	else:
		print(second_name, third_name, first_name)