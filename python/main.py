import keyboard
import time

def press_key(key):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)

def keypress_a():
    press_key('a')

def keypress_b():
    press_key('b')

def key_loop(key_funcution):
    try:
        while True:
            key_funcution()
    except KeyboardInterrupt:
        print("Exiting")
key_loop(keypress_a)

"""
# Original version (not functional programming)
def keyboardpress():
    keyboard.press(a)
    time.sleep(10)
    keyboard.press(b)
    keyboard.release(a)
    keyboard.release(b)

# Reasons:
# A. It doesn't treat functions as first-class citizens.
# B. It has side effects instead of being a function with no side effects.
"""

"""
# Refactored version (following functional programming)
def press_key(key):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)

# Reasons:
# A. It has no side effects and allows other functions to use it with the variable "key".
# B. It treats functions as first-class citizens by encapsulating key press and release actions.
# Also, this is better; 1, It looks cleaner and more concise and 2, It's interchangable
"""