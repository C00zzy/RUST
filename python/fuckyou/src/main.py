import random
import os
def numbers():
    while True:
        try:
            print(random.randrange(3, 20))
        except KeyboardInterrupt:
            print("stopped")
            break
numbers()