with open("Unit 09/test.txt",'r') as fp:
    lines = [line.strip() for line in fp]

print(lines)
print()

for line in lines: 
    print(line.split())
