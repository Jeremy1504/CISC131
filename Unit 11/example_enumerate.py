# create a list
lst = [12345, 54321, '13579', 'HW']
print(lst)

# iterate and returns an enumerate object with a counter variable and related element
for idx, value in enumerate(lst):
    print(idx, value)

print()

# create a dictionary
book = {}
book['title'] = 'starting out with python'
book['author'] = 'Tony Gaddis'
book['price'] = 50
book['ISBN'] = ['0133862259', '978013386225']

# enumerate also works on a collection, such as a dictionary
# iterate and returns an enumerate object with a counter variable and related element
for idx, key in enumerate(book):
    print(idx, key)

print()

for idx, (key, value) in enumerate(book.items()):
    print(idx, key, value)
