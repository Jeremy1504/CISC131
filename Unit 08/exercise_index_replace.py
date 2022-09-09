# a list of strings
animal = ['bird', 'tiger', 'dog', 'cat', 'fish', 'bear']
print(animal)
print()


# search key-word
word = 'fish'

# check membership
if word in animal:
    # if founded, find the word's index
    # and modify it's value with 'dear'
    animal[animal.index(word)] = 'deer'


# re-print the list
print(animal)



# alternatively, use a for loop
animal = ['bird', 'tiger', 'dog', 'cat', 'fish', 'bear']
for item in animal:
    if item == 'fish':
        idx = animal.index(item)
        animal[idx] = 'deer'

print(animal)
    