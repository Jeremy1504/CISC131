fp = open("Unit 09/test.txt", "r")    
content = fp.read()

myList = content.split()

print(myList)

fp.close()
