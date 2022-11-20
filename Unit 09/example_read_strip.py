
fp = open("Unit 09/test.txt", "r")    
content = fp.read()

# read data and store it as a long string
lines = content.strip()

print(lines)
print(len(lines))

fp.close()
