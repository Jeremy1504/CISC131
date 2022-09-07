def string_index():
    raw_input = input('Please Enter a string: ')
    idx = int(input('Please Enter the index number: '))

    try:
        return raw_input[idx]
    except IndexError:
        print('Index out of range!')

print(string_index())
