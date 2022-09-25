book = {}
book['title'] = 'starting out with python'
book['author'] = 'Tony Gaddis'
book['price'] = 50
book['ISBN'] = ['0133862259', '978013386225']
print(book)

print()
# print all keys
for key in book:
    print(key)

print()
# print all keys, and key's values
for key in book:
    print(key, book[key])

