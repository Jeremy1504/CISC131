book = {}
book['title'] = 'starting out with python'
book['author'] = 'Tony Gaddis'
book['price'] = 50
book['ISBN'] = ['0133862259', '978013386225']

# get() returns a value from a key
print(book.get('price'))
# alternatively, using [] operator
print(book['price'])

print()
# items() returns all keys and values
print(book.items())

print()
# iterate over a dictionary's keys and values
for item in book.items():
    print(item)

print()
# iterate over a dictionary's keys only
for key in book.keys():
    print(key)
    
print()
# iterate over a dictionary's values only
for value in book.values():
    print(value)
