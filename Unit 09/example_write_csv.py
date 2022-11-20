import csv
row_list = [['SN', 'Name', 'Contribution'],
            [1, 'Bill Lubanovic', 'Introducing Python'],
            [2, 'Tony Gaddis', 'Starting out with Python', ],
            [3, 'Gayle L. Mcdowell', 'Cracking the Coding Interview']]

with open('Unit 09/books.csv', 'w', newline='') as fp:
    csv_writer = csv.writer(fp)
    csv_writer.writerows(row_list)
