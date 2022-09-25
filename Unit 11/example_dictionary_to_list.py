book = {}
book['title'] = 'starting out with python'
book['author'] = 'Tony Gaddis'
book['price'] = 50
book['ISBN'] = ['0133862259', '978013386225']
print(book)

# convert a dictionary to a list of tupples
items = list(book.items())
print(items)

# convert a dictionary's keys to a list
keys = list(book.keys())
print(keys)

# convert a dictionary's values to a list
values = list(book.values())
print(values)

print()