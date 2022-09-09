animal = ['bird', 'tiger', 'dog', 'cat', 'fish', 'bear']

def find_animal(lst):

    word = input('Please Enter an animal name: ')


    if word in lst:
        lst[lst.index(word)] = 'deer'

    lst.remove('bear')

    return lst

print(find_animal(animal))
