import os

def screenclear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def logic():
    screenclear()
    try:
        pounds = (float(input("What is your weight in Pounds: ")))
        result = pounds * 0.45359237
        print(result)
    except ValueError:
        print("invalid")
logic()
