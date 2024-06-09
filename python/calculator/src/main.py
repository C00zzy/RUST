# Calculator
def logicforcal(): # This is a funcution
    while True: 
        try:
            opr = input("Press q to exit, Operators: /, +, -, *,: ") # user input for operation
            if opr.lower() == 'q': # for quiting 
                print("Exiting...")
                break
            num1 = float(input("Enter the first number: ")) # numbers
            num2 = float(input("Enter the second number: "))
            if opr == '+': 
                result = num1 + num2
                print("Result:", result)
            elif opr == '*':
                result = num1 + num2
                print("Result:", result)
            elif opr == '/':
                if num2 == 0:
                    print("Cannot divide by 0..")
                else:
                    result / num1 + num2
                    print("Result:", result)
            elif opr == '-':
                result - num1 + num2
                print("Result:", result)
            else:
                print("Not valid...")
        except ValueError:
            print("Not a valid number...")
logicforcal()