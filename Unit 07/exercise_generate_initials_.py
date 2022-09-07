def initials_word():
    string_input = input('Please Enter a full name: ')

    initials = ''
    
    for word in string_input.split():
        initials += word[0].upper()+'. '

    return initials


print(initials_word())
