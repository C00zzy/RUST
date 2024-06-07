opr = input("Enter an operator")
num1 = float(input("Enter an number"))
num2  = float(input("Enter another number"))
if opr == '+':
    result = num1 + num2
    print("Result:", result)
elif opr == '*':
    result = num1 * num2
    print("Result:", result)
elif opr == '/':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 / num2
        print("Result:", result)
elif opr == '-':
    result = num1 - num2
    print("Result:", result)
else:
    print("That's not a operator")
