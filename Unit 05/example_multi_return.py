def main():
    print('The result is:')
    result, num1, num2 = cal_product(3, 15)
    print(result, num1, num2)

def cal_product(num1,num2):
    result = num1 * num2
    return result, num1, num2

main()
