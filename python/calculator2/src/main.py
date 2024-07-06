
# First Funcution

def getnum():
    while True:
        try:
            num1, num2 = input("Two numbers").split(',')
            num1 = float(num1.strip())
            num2 = float(num2.strip())
            return num1, num2
        except KeyboardInterrupt:
            print("Leaving")
            break
        except ValueError:
            print("Invalid")
# Second Funcution
def addition(num1, num2):
    return num1 + num2
# Third Funcution
def substraction(num1, num2):
    return num1 - num2
# Fourth Funcution
def dividison(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return("ERROR")
# Fifth Funcution
def multi(num1 ,num2):
    return num1 * num2
def calculate(opr, num1, num2):
    if opr == '+':
        return addition(num1, num2)
    if opr == '*':
        return multi(num1, num2)
    if opr == '/':
        return dividison(num1, num2)
    if opr == '-':
        return substraction(num1, num2)
    else:
        return ("Invalid")
def calculator():
    opr = get_opr()
    num1, num2 = getnum()
    solution = calculate(opr, num1, num2)
    print(solution)
def get_opr():
    while True:
            opr = input("Enter opr")
            if opr in ['+', '*', '/', '-']:
                return opr
            else:
                print("Error")
calculator()
#redone with funcutional programming