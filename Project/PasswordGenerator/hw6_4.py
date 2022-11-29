import string
import random

def generateString(n):
    return ''.join(random.choices(string.ascii_letters, k=n))

generateString(8)
