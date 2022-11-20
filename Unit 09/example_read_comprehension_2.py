with open("Unit 09/test.txt",'r') as fp:
    lines = [line.strip() for line in fp]

# reverse sentence
for line in lines[::-1]: 
    print(line)

# for line in lines[::-1]: 
#     print(line.split())