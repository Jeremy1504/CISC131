# create an empty set
my_set = set()

for i in range(1, 6):
    # add number to set
    my_set.add(i)

print(my_set)

# remove item from set
my_set.remove(1)
print(my_set)

for item in my_set:
    print(item)
