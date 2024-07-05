# Modules
import sys
import keyboard # Needs pip and a virtual enviroment to install
import time
import os
def rootstatus():
    return os.getuid() == 0 # This checks if user is root: Typically 0 on Linux systems 

def shortcut(key): # Main Funcution
    while True:
        keyboard.press(key)#
        time.sleep(0.1)
        keyboard.release(key)

if not rootstatus():
    print("Run as root")
    sys.exit(1) # Returns 1 if user is not root

key = input("What do you want to be: ")
shortcut(key)