import os

def screenclear():
    if os.name == 'posix':
        os.system('clear')
    if os.name == 'nt':
        os.system('cls')

def userinput():
    screenclear()
    n = int(input("What number: "))
    solution = factorinal(n)
    print(f"the factoral of {n} is: {solution}")
def factorinal(n):
    if n == 0:
        return 1
    else:
        return n * factorinal(n - 1)
userinput()


