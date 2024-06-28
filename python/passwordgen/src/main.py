# Modules
import random
import string
from typing import Literal

# Funcution

def randomletterandnums() -> None:
    password: Literal[''] = ""
    for _ in range(10):
        randomnum: int = random.randrange(start=1, stop=30)
        randomlet: str = random.choice(seq=string.ascii_letters)
        password += str(object=randomnum) + randomlet
    print(password)

randomletterandnums()