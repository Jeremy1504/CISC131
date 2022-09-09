# method 1: create and append
lst_1 = [1,2,3,4]
lst_2 = []

# use loop to iterate over a list
for i in lst_1:
    # append each element to the new list
    lst_2.append(i)
lst_2[0] = 100
print(lst_2)
print(lst_1)


# method 2: create and concatenate
lst_1 = [1,2,3,4]
lst_2 = []

# concatenate whole list to a new list
lst_2 += lst_1
lst_2[0] = 100
print(lst_2)
print(lst_1)
