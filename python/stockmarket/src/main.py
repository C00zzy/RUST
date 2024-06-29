import os
# Stock market script concept
def screenclear(): # This is a command line program
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


def checkcandleinput(): # for input funcution
    while True:
        candle = input("Green for 1, Red for 0: ")
        if candle in ["0", "1"]: # Checks if the input is 1 or 0 and if so candle is assigned to that
            return candle # Returns to outside of funcution
        else:
            print("Invalid")


def check_candle() -> None:
    candle: str = checkcandleinput()
    if candle == "1":
        print("INVEST") # Main Logic
    elif candle == "0":
        print("STOP")
screenclear()
check_candle()
