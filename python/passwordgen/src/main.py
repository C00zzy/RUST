import random
import string

def randomletterandnums() -> None:
    n = int(input("How long do you want your password: "))
    password = ""
    for _ in range(n): # does this until it hits the quota
        randomnum: int = random.randrange(start=1, stop=10) # Generates numbers
        randomlet: str = random.choice(seq=string.ascii_letters) # Generates lettersj
        password += str(object=randomnum) + randomlet # Adds them together
    print(password)

randomletterandnums()