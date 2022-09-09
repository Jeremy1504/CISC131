lst_1 = [1,2,3,4]
# reference the same memory address
lst_2 = lst_1

# modify element will affect the reference
lst_2[0] = 100
print(lst_2)
print(lst_1)
