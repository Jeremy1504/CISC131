def key_argument(num1, num2, num3):
    result = num1 + num2 - num3
    print(result)


number1 = 10
number2 = 20
number3 = 5

key_argument(number1, number2, number3)
key_argument(num2=100, num3=30, num1=10)
key_argument(10, num3=30, num2=100)
