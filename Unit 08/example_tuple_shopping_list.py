# this is a demo function that find text item from a dictionary
# and return its price
def find_price(item):
    # a dictionary that stores the price of food
    price_table = {'bread': 5.47, 'milk': 4.68, 'egg':1.83, 'meat': 5.99}
    
    # return the price value only
    return price_table[item]


shopping_list = ['bread', 'milk', 'egg', 'meat']

total = 0
for item in shopping_list:
    # call another function and return its price
    total += find_price(item)
print(total)

