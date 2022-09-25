book = {}
book['title'] = 'starting out with python'
book['author'] = 'Tony Gaddis'

edition = ['3rd', '4th']
book[edition] = '3/4 edition'

book[('edition')] = edition

print(book['title'])
print(book['edition'])
print(book['ISBN'])
