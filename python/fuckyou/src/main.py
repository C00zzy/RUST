import random
def numbers():
    while True:
        try:
            print(random.randrange(3, 100000))
        except KeyboardInterrupt:
            print("stopped")
            break
numbers()