count = 0

words = input('Enter a word: ')
for c in words:
    # count if the current character is a 'e'
    if c == 'e':
        # if so, counter variable increase 1
        count += 1

print(count)

print()
############################################
count = 0

# repeat 3 times
for i in range(0, 3):
    words = input('Enter a word: ')
    # nested for loop
    for c in words:
        # count if the current character is a 'e'
        if c == 'e':
            # if so, counter variable increase 1
            count += 1

print(count)
