# modules
import random
import string
import typing
# funcution

def randomletterandnums() -> None:
    password = ""
    for _ in range(10): # does this until it hits the quota
        randomnum: int = random.randrange(start=1, stop=10) # Generates numbers
        randomlet: str = random.choice(seq=string.ascii_letters) # Generates lettersj
        password += str(object=randomnum) + randomlet # Adds them together
    print(password)

randomletterandnums()