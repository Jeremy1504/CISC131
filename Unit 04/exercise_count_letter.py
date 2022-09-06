count = 0

for i in range(0, 3):
    words = input('Enter a word: ')
    
    for c in words:
        if c == 'e':
            count += 1

print(count)
