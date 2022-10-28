def validInput(score):
    # use a function to check input validation
    try:
        if score < 0 or score > 100: # if score is out of range, throw a ValueError
            raise ValueError(score)
    except ValueError: # catch ValueError
        print('value error') # print an error message
    else: # if there is no error, print the score
        print(score)

validInput(90)
validInput(101)
validInput(-10)
