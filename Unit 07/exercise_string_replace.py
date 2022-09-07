my_str = "~%I am a @developer & musician!!"

# method 1
def replaceString(s):
    for c in s:
        if not c.isalpha():
            s = s.replace(c, '#')
    return s

print(replaceString(my_str))

# method 2 using string library
import string

my_str_2 = "~%I am a @developer & musician!!"

def replaceString2(s):

    special_str = string.punctuation

    for c in special_str:
        s = s.replace(c, '#')
    return s

print(replaceString2(my_str_2))

my_str_3 = "~%I am a @developer & musician!!"

# method 3
def replaceString3(s):
    new_string = ''
    for c in s:
        if not c.isalpha():
            new_string += c.replace(c, '#')
        else:
            new_string += c


    return new_string

print(replaceString3(my_str_3))
