import random
import string
import os

def screenclear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
def numloop():
    column = 80
    while True:
        try:
            print(random.randrange(1, 1000))
        except KeyboardInterrupt:
            screenclear()
            break
numloop()