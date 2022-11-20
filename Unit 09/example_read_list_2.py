fp = open("Unit 09/test.txt", "r")
content = fp.read()
fp.close()

# split with \n lines 
myList = content.split('\n')

print(myList)
print()
print(myList[0])
