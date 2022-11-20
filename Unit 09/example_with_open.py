with open('Unit 09/test.txt','r') as fp:
    content = fp.read()
print(content)

# equivalent
print()
fp = open('Unit 09/test.txt','r')
content = fp.read()
fp.close()
print(content)
