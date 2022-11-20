myList = []

#Open OutputFile.txt in read mode
inputFile = open("Unit 09/test.txt", "r")    

#For each line in the file
for line in inputFile:  
    #Add the line to myList, stripping out whitespace
    myList.append(line.strip()) 

print(myList)
print()
print(myList[0])

inputFile.close()
