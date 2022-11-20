myList = []

fp = open("Unit 09/test.txt", "r")    
content = fp.read()

for word in content.split():
    myList.append(word.upper()) 

print(myList)

fp.close()
