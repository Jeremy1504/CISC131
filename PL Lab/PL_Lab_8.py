import csv
import random


def read_avg(filename):

    # generate file
    # using with to make sure file will be closed automatically
    with open(filename, 'w') as fp:
        # generate 100 numbers
        for i in range(100):
            # convert random number into string and append a white space for each number
            content = str(random.randint(1, 5)) + ' '
            # write the whole content
            fp.write(content)

    # open generated file

    with open(filename, 'r') as fp:
        content = fp.read()

    length = 0
    sum_up = 0

    # read() will return an string, use split() to convert into a list
    for item in content.split():
        # string to integer
        sum_up += int(item)
        length += 1

    print('The average is ', sum_up/length)


read_avg('number.txt')


###########################################################

def compareAnswers(file1, file2):

    correct = []
    student = []

    with open(file1) as fp:
        student = fp.read().split()

    with open(file2) as fp:
        correct = fp.read().split()

    count = 0
    num = len(correct)

    for idx in range(num):
        if student[idx] == correct[idx]:
            count += 1

    return count


print('Correct Answers:', compareAnswers('answers.txt', 'correct_answers.txt'))

###########################################################


def separateString(filename):

    try:
        with open(filename, 'r') as fp:
            content = fp.read()

        letter = ''
        digit = ''
        symbol = ''

        for item in content:
            if item.isalpha():
                letter += item
            elif item.isdigit():
                digit += item
            else:
                symbol += item
        print(letter, digit, symbol)
    # catch error
    except FileNotFoundError as err:
        print(err)


separateString('test.txt')

###########################################################


def combineFiles(file_name1, file_name2, file_output):

    # initialize empty strings
    data1 = ''
    data2 = ''

    # open file and assign variables
    with open(file_name1, 'r') as fp:
        data1 = fp.read()

    with open(file_name2, 'r') as fp:
        data2 = fp.read()

    # concatenate content
    data1 += data2

    # save file on disk
    with open(file_output, 'w') as fp:
        fp.write(data1)

    # debug use
    print('Done')


combineFiles('sonnet_1.txt', 'sonnet_2.txt', 'sonnet.txt')

###########################################################

# use read() method


def lineNum(filename):
    # open file with encoding utf-8 to avoid Mojibake issue
    with open(filename, 'r', encoding='utf-8') as fp:
        content = fp.read()

    count = 0
    for item in content.split('\n'):
        print('{}: {}'.format(count+1, item))
        count += 1


lineNum('sonnet.txt')


# # use readlines() method
# def lineNum(filename):
#     # open file
#     with open(filename, 'r', encoding='utf-8') as fp:
#         content = fp.readlines()

#     content = [x.strip() for x in content]

#     count = 0
#     for item in content:
#         print('{}: {}'.format(count+1, item))
#         count += 1

# lineNum('sonnet.txt')

###########################################################

# Skip this, too challenging
# def spaceCost(filename):
#     try:
#         with open(filename, 'r') as fp:
#             # use csv library
#             # csv.reader()
#             content = csv.reader(fp)
#             # csv.reader() returns an object
#             # convert it to a list of lists
#             data = list(content)
#     # just in case of file error
#     except FileNotFoundError as err_io:
#         print(err_io)

#     try:
#         # print & preview data
#         # get a basic sense about our data
#         print(['Living Space (sq ft)',  'Year', 'List Price ($)'])
#         for row in data:
#             print(row)

#         # calculation
#         total_space = 0
#         total_price = 0

#         for i in range(len(data)):
#             # 2-D lists
#             # space is on 1nd column which is index 0
#             # price is on 3rd column which is index 2
#             total_space += int(data[i][0])
#             total_price += int(data[i][2])

#         print('Average Price ($/sq ft): ', total_price/(total_space))

#     # just in case of invalid data
#     except (ValueError, ZeroDivisionError, TypeError) as err:
#         print(err)


# spaceCost('zillow.csv')
