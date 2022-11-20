import csv

filename = "Unit 09/data/ford_escort.csv"

data = []

with open(filename, 'r') as fp:
    csv_reader = csv.reader(fp)

    for row in csv_reader:
        data.append(row)

# preview data
# for row in data:
#     print(row)


######################
# Clean up
######################

# extract header field which is the first row
header = data[0]
print('Header of data: ')
print(header)
print()
# remove the first row from data
del data[0]

# data.pop(0)

# preview data
for row in data:
    print(row)

# convert all string to integer
data = [[int(j) for j in i] for i in data]

# clean data
for row in data:
    print(row)

######################
# Data Analysis
######################

# calculate avg price
total = 0
row_length = len(data)

for i in range(row_length):
    # second column
    total += data[i][2]


print('Avg price for Ford Escort ($): ', total/row_length)