lst = [1, 2, 3, 4, 5]
result = [x ** 2 for x in lst]
print(result)

test = [x for x in lst if x % 2 == 0]
print(test)


# element-wise operations
# method 1: loop with index
lst_1 = [1, 2, 3, 4]
lst_2 = [5, 6, 7, 8]


res_lst = []
for i in range(len(lst_1)):
    res_lst.append(lst_1[i]+lst_2[i])
print(res_lst)
