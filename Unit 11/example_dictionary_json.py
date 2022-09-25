import json

book = {}
book['title'] = 'starting out with python'
book['author'] = 'Tony Gaddis'
book['price'] = 50
book['ISBN'] = ['0133862259', '978013386225']

# write a json file on hard disk
with open('book.json', 'w') as json_file:
  json.dump(book, json_file)

# read a json file
with open('book.json') as fp:
  data = json.load(fp)

# print content
print(data)

# Pretty printing JSON string back
print(json.dumps(data, indent = 4, sort_keys=True))
