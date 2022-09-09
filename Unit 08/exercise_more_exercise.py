test_list = [1, 5, 234, 43, -43, 190, 365, 363, -992]

def sum_list(lst):
    sum_up = 0
    for item in lst:
        sum_up += item

    return sum_up

def avg_list(lst):
    return sum_list(lst)/len(lst)

def reverse_list(lst):
    reverse_lst = lst[::-1]
    return reverse_lst

def max_list(lst):
    return max(lst)

def second_max_list(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[-2]

def replace_list(lst):
    replaced_lst = []
    for item in lst:
        if item<=0:
            replaced_lst.append(-item)
        else:
            replaced_lst.append(item)
    return replaced_lst

def separate_list(lst):
    list_odd = []
    list_even = []

    for item in lst:
        if item %2 == 0:
            list_even.append(item)
        else:
            list_odd.append(item)
    return list_odd, list_even

# test statements
print(test_list)
print(sum_list(test_list))
print(avg_list(test_list))

reverse_lst = reverse_list(test_list)
print(reverse_lst)

print(max_list(test_list))
print(second_max_list(test_list))

replaced_lst = replace_list(test_list)
print(replaced_lst)

odd_lst, even_lst = separate_list(test_list)
print(odd_lst)
print(even_lst)

print(test_list)




