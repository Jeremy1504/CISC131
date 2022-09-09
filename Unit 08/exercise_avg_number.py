test_list = [1, 5, 234, 43, -43, 190, 365, 363, -992]

def avg_list(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

print(avg_list(test_list))