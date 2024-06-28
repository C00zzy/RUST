# Modules
import random
import string
from typing import Literal

# Funcution

def randomletterandnums() -> None:
	password = []
	for _ in range(10):
		randomnum: int = random.randint(1, 29)
		randomlet: str = random.choice(string.ascii_letters)
		password.append(f'{randomnum}{randomlet}')
	print("". join(password))

randomletterandnums()