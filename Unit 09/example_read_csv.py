import csv

data = []

with open('Unit 09/data/ford_escort.csv','r') as fp:
    # csv.reader() method
    csv_reader = csv.reader(fp)

    # append data into a list of list
    for row in csv_reader:
        data.append(row)

# print list of list by row
for row in data:
    print(row)