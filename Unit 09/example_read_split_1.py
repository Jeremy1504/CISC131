
fp = open("test.txt", "r")    
content = fp.read()

myList = content.split()

print(myList)

fp.close()
