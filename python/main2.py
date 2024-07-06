import random

def printforvalue(value):
    print(value)

def forloop(start, end, func,):
    for i in range(start, end + 1):
        func(i)

forloop(1, 200, printforvalue)