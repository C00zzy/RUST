def logicforcal():
    while True:
        try:
            opr = input("Enter an operator")
            if opr.lower() == 'q':
                print("Exiting")
                break
            num1 = float(input("Enter an number"))
            num2 = float(input("Enter an number"))
            
            if opr == '+':
                result = num1 + num2
                print("Result:", result)
            elif opr == '*':
                result = num1 + num2
                print("Result:", result)
            elif opr == '/':
                if num2 == 0:
                    print("Cannot divide by 0")
                else:
                    result / num1 + num2
                    print("Result:", result)
            elif opr == '-':
                result - num1 + num2
                print("Result:", result)
            else:
                print("Not valid")
        except ValueError:
            print("Not a valid number")
logicforcal()