# a list to store vowel letters
vowels_lst = ['a', 'e', 'i', 'o', 'u', 'y']

# test example
test_string = 'apple'

# initialize a counter variable with 0
count = 0

# a for loop to iterate over each character from a list
for c in test_string:
    # if this character is a member of vowel_lst
    if c.lower() in vowels_lst:
        # then, our counter increase by 1
        count += 1

# print the final counter variable
print(count)
