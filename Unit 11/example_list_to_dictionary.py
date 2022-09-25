# a list to a dictionary
lst=['title','author','price','ISBN']
book=dict(enumerate(lst))
print(book)

# two lists to a dictionary
keys = ['title', 'author', 'price', 'ISBN']

values = ['starting out with python', 
	'Tony Gaddis', 50, '0133862259']

# zip() construct a dictionary
book = dict(zip(keys, values))

print(book)
