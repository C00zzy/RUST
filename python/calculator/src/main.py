# Calculator

def logicforcal(): # Define a function for calculator logic
    while True: # Keep the calculator running until the user decides to exit
        try:
            opr = input("Press q to exit, Operators: /, +, -, *,: ") # Prompt user for operation choice
            if opr.lower() == 'q': # If user inputs 'q', exit the calculator
                print("Exiting...")
                break
            num1 = float(input("Enter the first number: ")) # Prompt user for the first number
            num2 = float(input("Enter the second number: ")) # Prompt user for the second number
            if opr == '+': # Addition operation
                result = num1 + num2 # Perform addition
                print("Result:", result) # Print the result
            elif opr == '*': # Multiplication operation
                result = num1 * num2 # Perform multiplication
                print("Result:", result) # Print the result
            elif opr == '/': # Division operation
                if num2 == 0: # Check if second number is zero (division by zero check)
                    print("Cannot divide by 0..") # Print error message
                else:
                    result = num1 / num2 # Perform division
                    print("Result:", result) # Print the result
            elif opr == '-': # Subtraction operation
                result = num1 - num2 # Perform subtraction
                print("Result:", result) # Print the result
            else:
                print("Not valid...") # If the operation is not one of the specified ones, print error message
        except ValueError:
            print("Not a valid number...") # If user inputs a value that cannot be converted to a number, print error message

logicforcal()
