def findMax(lst):
    largest = -9999999
    for i in lst:
        if i > largest:
            largest = i
    return largest

lst = [3, 10, 5, 22, 31, -23, -31]

print(findMax(lst))
