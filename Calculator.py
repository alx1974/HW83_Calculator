#HW83 Calculator
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
operation = input("Enter math operation ( + | - | * | / ) : ")
if operation == "+":
    result = int(number1)+int(number2)
elif operation == "-":
    result = int(number1) - int(number2)
elif operation == "*":
    result = int(number1) * int(number2)
elif operation == "/":
    result = int(number1) / int(number2)
else:
    print("You did not enter a correct operator!!")
    exit()
print(result)
