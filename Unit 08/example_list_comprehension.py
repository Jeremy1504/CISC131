# list comprehension to generate sequence
seq = [2 ** x for x in range(10)]
print(seq)

# equivalent expression
lst = []
for x in range(10):
    lst.append(2 ** x)
print(lst)


# list comprehension with .lower() method
lst = ["Hello", "World", "CISC", "131"]

# convert each item in a list to its lower-case
new_lst = [x.lower() for x in lst]
print(new_lst)

