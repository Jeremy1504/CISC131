def countString(s):
    count_digit = 0
    count_letter = 0
    for c in s:
        if c.isdigit():
            count_digit += 1
        if c.isalpha():
            count_letter += 1
    return count_digit, count_letter

print(countString('CISC131'))

print(countString('abc_123-def'))

