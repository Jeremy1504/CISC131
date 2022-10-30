def findVowels(s):
    vowels = 'aeiouAEIOUyY'
    count = 0
    for c in s:
        if c in vowels:
            count += 1

    return count

print(findVowels('Halloween'))
print(findVowels('Thanksgivings'))