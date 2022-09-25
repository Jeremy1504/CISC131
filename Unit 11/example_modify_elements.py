# add elements to an existing dictionary
phoneBook = {}
print(phoneBook)

# add a key-value pair
phoneBook['Smith'] = '12345'
print(phoneBook)

phoneBook['Joe'] = '5001'
print(phoneBook)

# modify value for a key
phoneBook['Smith'] = '54321'
print(phoneBook)


######################################
print()
######################################

del phoneBook['Smith']
print(phoneBook)
