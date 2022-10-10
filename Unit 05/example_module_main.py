# example_module_avg.py is in the same directory
# from the moudle and import the avgTwo() function
from example_module_avg import avgTwo

def main():
    print('Hello World')

    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))

    avg = avgTwo(num1, num2)

    print(avg)

main()