import os 

def screenclear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def get_numbers():
    while True:
        try:
            num1, num2, = input("Enter two number seperated by a comma:  ").split(',')
            
            num1 = float(num1.strip())
            num2 = float(num2.strip()) 
            
            return num1, num2
        except ValueError:
            print("Invalid")

def addition(num1, num2):
    return num1 + num2

def multiplication(num1, num2):
    return num1 * num2

def divde(num1, num2):
    return num1 / num2

def substract(num1, num2):
    return num1 - num2
    
def userinput(num1, num2):
    input = ("Enter an operator!:  ")
    
def get_opr():
    while True:
        opr = input("Enter operator:  ")
        if opr in ['+', '*', '/', '-']:
            return opr
        else:
            print("invalid")
def calculator():
    operator = get_opr()
    num1, num2 = get_numbers()
    if operator == '+':
        solution = addition(num1, num2)
        print(solution)
    elif operator == '*':
        solution = multiplication(num1, num2)
        print(solution)
    elif operator == '/':
        solution = divde(num1, num2)
        print(solution)
    elif operator == '-':
        solution = substract(num1, num2)
calculator()