# use list data structure
def compareAnswers(file1, file2):
    
    correct = []
    student = []
    
    with open(file1) as fp:
        correct = fp.read().split()
    fp.close()
    
    with open(file2) as fp:
        student = fp.read().split()
    fp.close()
    
    count = 0
    num = len(correct)
    
    for idx in range(num):
        if student[idx] == correct[idx]:
            count +=  1
    
    return count

print(compareAnswers('Unit 09/demo85_1.txt', 'Unit 09/demo85_2.txt'))

# not using list, use obj
def compare_file(file1, file2):

    f1 = open(file1, 'r')
    f2 = open(file2, 'r')

    count = 0
    for line1 in file1:
        for line2 in file2:
            if line1.strip() == line2.strip():
                count += 1
    f1.close()
    f2.close()
    
    return count

print(compare_file('Unit 09/demo85_1.txt', 'Unit 09/demo85_2.txt'))
