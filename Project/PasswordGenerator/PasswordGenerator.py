import random

def generatePassword(n):
    '''
    A simple function to generate strong password in a given length
    - n: length of passowrd
    - output: return the password 
    '''
    # input validation
    # length should be at least 8 characters
    while n < 8:
        n = int(input('Length should be no lower than 8. Re-enter (n):'))

    else:
        # character set
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = lower.upper()
        num = '1234567890'
        symbol = '~!@#$%^&*_-+=`|\(){}[]:;<>,.?/'
        # a long string that contains all candidate characters
        random_source = lower + upper + num + symbol

        password = ''
        # pick at least one character from the candidate set
        # pick at least one lower, one upper, one number, one special character
        password += random.choice(lower)
        password += random.choice(upper)    
        password += random.choice(num)
        password += random.choice(symbol)

        # fill in the rest of the characters
        for i in range(n - 4):
            password += random.choice(random_source)

        # shuffle only works on a list
        password_lst = list(password)
        random.shuffle(password_lst)
        
        # convert list back to string
        return ''.join(password_lst)

# test cases
print(generatePassword(8))
print(generatePassword(10))
print(generatePassword(13))
