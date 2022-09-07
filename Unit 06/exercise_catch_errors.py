try:
    print(undeclared_variable)
    print(1 / 0)
    print("No error occurred!")
except NameError:
    print("A NameError occurred!")
except ZeroDivisionError:
    print("A ZeroDivisionError occurred!")
print("Done!")

