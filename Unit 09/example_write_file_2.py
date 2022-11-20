myInt1 = 10
myInt2 = 20

#Open OutputFile.txt in write mode
outputFile = open("Unit 09/OutputFile.txt", "w")    

#Write myInt1, myInt2 to outputFile
outputFile.write(str(myInt1)+'\n')

outputFile.write(str(myInt2))    

#Close outputFile
outputFile.close() 
