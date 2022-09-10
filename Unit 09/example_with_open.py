with open('test.txt','r') as fp:
    content = fp.read()
print(content)

# equivalent
print()
fp = open('test.txt','r')
content = fp.read()
fp.close()
print(content)
