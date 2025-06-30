operator = input("Enter the word that describes your math operation: ")
operand1 = int(input("Enter the first number: "))
operand2 = int(input("Enter the second number: "))


if operator == "add":
    print(f"{operand1} + {operand2} = {operand1 + operand2}" )
elif operator == "subtract":
    print(f"{operand1} - {operand2} = {operand1 - operand2}" )
elif operator == "multiply":
    print(f"{operand1} * {operand2} = {operand1 * operand2}" )
elif operator == "divide":
    if operand2 != 0:
        print(f"{operand1} / {operand2} = {operand1 / operand2}" )
    else:
        print("Can't divide by zero")
else: 
    print("Unknown operation")