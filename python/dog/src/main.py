import os

def screenclear():
    if os.name == 'posix':
        os.system('clear')
    if os.name == 'nt':
        os.system('cls')

def getnum():
    screenclear()
    age = int(input("What is your age"))
    result = calculation(age)
    print(result)


def calculation(age):
    return age * 7

getnum()
#comments made by AI
