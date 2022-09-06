def findMax(*lst):
    largest = -9999999
    for i in lst:
        if i > largest:
            largest = i
    return largest

print(findMax(1, 10, 15, 32, -90, 25))

