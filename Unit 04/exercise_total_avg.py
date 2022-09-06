n = 3

total = 0
count = 0

for i in range(1, n+1):
    value = float(input('Please enter a number: '))

    count += 1
    total += value

print('Total : ', total)
print('Average : ', total/count)
