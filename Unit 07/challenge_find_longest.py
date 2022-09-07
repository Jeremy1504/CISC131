def longest_word():
    string_input = input('Please Enter a sentence: ')

    longest_word = ''

    for word in string_input.split():
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


print(longest_word())
