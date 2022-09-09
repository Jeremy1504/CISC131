test_list = [1, 5, 234, 43, -43, 190, 365, 363, -992]

def abs_value(lst):
    new_lst = []
    for num in lst:
        if num >= 0:
            new_lst.append(num)
        else:
            new_lst.append(-num)

    return new_lst

print(abs_value(test_list))