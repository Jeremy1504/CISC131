#####################################################################
# Lab 6-1: string operations
#####################################################################

def swapCharacter(s):
    # string index and string slicing
    # the last character + middle characters + the first character
    return s[-1]+s[1:-1]+s[0]

print(swapCharacter('abcdef'))


def mixedString(s1, s2):

    # middle index number of s1
    mid = int(len(s1) / 2)

    # get character from 0 to the middle index number from s1
    s3 = s1[:mid:]
    # concatenate s2 to it
    s3 = s3 + s2
    # append remaining character from s1
    s3 = s3 + s1[mid:]
    return s3

print(mixedString('Computer', 'Science'))


def replaceCharacter(s):
    # use a variable to store the first character
    letter = s[0]
    # use another variable, empty string, will concatenate it for later use
    replace_s = ''

    # iterate input string
    for i in s:
        # if found this character
        if i == letter:
            # repalce it with a '$'
            replace_s += '$'
        else:
            # otherwise, concatenate it with the original character
            replace_s += i
    # the output contains two components: the first character; the replaced string starting from the second characeter
    return letter+replace_s[1:]


print(replaceCharacter('abcabcabcabc'))

#####################################################################
# Lab 6-2: string methods
#####################################################################

def splitString(s):

    # split string by hyphen '-'
    sub_strings = s.split("-")
    # iterate the sub strings and print each item per line
    for sub in sub_strings:
        print(sub)

splitString('I-am-a-software-engineer!')
splitString('I-am-a-data-scientist!')
splitString('I-am-a-network-engineer!')

def digitStrings(s):
    # initialize two accumulater variables
    total = 0
    count = 0
    # iterate each character in given input string
    for char in s:
        # first, check whether this character is a digit or not
        if char.isdigit():
            # if so, increase 1 for count, increase this char for total, make type conversion
            total += int(char)
            count += 1
    try:
        # calculate avg
        avg = total / count
    # catch ZeroDivisionError
    except ZeroDivisionError as err:
        # if caught zero division, print the error
        print(err)
        # and set avg with zero
        avg = 0
    # show final output
    print("Sum:", total, "\tAverage: ", avg)


digitStrings("CISC131_talent@2022 ")



def joinStrings():
    # since string is immutable
    # we can use an empty string and concatenate characters for later use
    join_word = ''
    
    # keep asking user to enter
    while True:
        word = input("Enter a word (Enter q or Q to quit): ")
        # will break the infinite loop when user enters Q or q
        if (word == 'Q') or (word == 'q'):
            break
        else:
            # otherwise, concatenate the previous string with capitalized word with a white space
            join_word = join_word + word.title() + ' '
    
    # return the final concatenated string
    return join_word

print(joinStrings())
