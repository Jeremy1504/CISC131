###########################################################
# Total Price

# use .values() method
def totalPrice(my_dictionary):
     
     total = 0
     for i in my_dictionary.values():
           total += i
      
     return total

# or using list() and sum()
def totalPrice(my_dictionary):
     
    list = []
    for i in my_dictionary:
        list.append(my_dictionary[i])
    total = sum(list)
     
    return total

# test case
purchasedBook = {'Starting out with Python': 50, 'Cracking the Coding Interview': 25, 'Python for Data Analysis': 28}
print(totalPrice(purchasedBook))

###########################################################
# Count Character

# use dictionary only
def countCharacter(s):
    all_freq = {}
    
    for char in s:
        if char in all_freq:
            all_freq[char] += 1
        else:
            all_freq[char] = 1

    return all_freq

print(countCharacter('Hello World'))

###########################################################
# Pair Two Lists


# use dictionary comprehension
def pairList(lst1, lst2):
    res = {lst1[i]: lst2[i] for i in range(len(lst1))}	
    return res

# use zip()
def pairList(lst1, lst2):
    res = dict(zip(lst1, lst2))
    return res

# test case
lst1 = ['AAPL', 'MSFT', 'AMZN', 'GOOGL']
lst2 = [160, 338, 3594, 2913]
print(pairList(lst1, lst2))


###########################################################
# Find Common Element

# use set()
def findCommon(lst1, lst2):
    # convert to set and remove dumplicates
    # then, convert back to list
    return list(set(lst1) & set(lst2))

lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

print(findCommon(lst1, lst2))