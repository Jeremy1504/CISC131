lst = [1, 2, [30, 40, [500, 600], 50], 3, 4]
print('original list: ', lst)

lst[2][2].append(700)
print('new list', lst)
