import random

def generatePassword(n):

    while n < 8:
        n = int(input('Length should be no lower than 8. Re-enter (n):'))

    else:
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = lower.upper()
        num = '1234567890'
        symbol = '~!@#$%^&*_-+=`|\(){}[]:;<>,.?/'

        random_source = lower + upper + num + symbol

        password = ''

        password += random.choice(lower)
        password += random.choice(upper)    
        password += random.choice(num)
        password += random.choice(symbol)
        
        for i in range(n - 4):
            password += random.choice(random_source)

        # shuffle only works on a list
        password_lst = list(password)
        random.shuffle(password_lst)
        
        # convert list back to string
        return ''.join(password_lst)


print(generatePassword(8))
print(generatePassword(10))
print(generatePassword(13))
