# use a list to store numbers
lst = []
# use loop and generate a sequence from 0 to 9
for i in range(10):
    # append each number
    lst.append(str(i))

print(lst)

# write and separate by comma
fp = open('Unit 09/num_test.txt', 'w')
fp.write(','.join(lst))
fp.close()

# write and separate by white space
fp = open('Unit 09/num_test.txt', 'w')
fp.write(' '.join(lst))
fp.close()

# write with appending mode and separate by white space
fp = open('Unit 09/num_test.txt', 'a')
fp.write('\n')
fp.write(' '.join(lst))
fp.close()

