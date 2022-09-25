grocery_lst = {'lettuce': 1.30, 'bread': 1.49, 'milk': 3.75, 
    'chicken breasts': 4.37, 'sirloin': 8.99, 'tomatoes': 1.99}


total = 0
for price in grocery_lst.values():
    total += price
print(total)

