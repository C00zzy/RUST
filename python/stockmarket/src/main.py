import os

def screenclear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


def checkcandleinput():
    while True:
        candle = input("Green for 1, Red for 0: ")
        if candle in ["0", "1"]:
            return candle
        else:
            print("Invalid")


def check_candle():
    candle = checkcandleinput()
    if candle == "1":
        print("INVEST")
    elif candle == "0":
        print("STOP")
screenclear()
check_candle()

