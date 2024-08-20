import random
import string

def PasswordGen():
    length = int(input("How long do you need the password to be?"))
    password = ""
    for _ in range(length): # does this until it hits the quota
        randomnum: int = random.randrange(start=1, stop=10) # Generates numbers
        randomlet: str = random.choice(seq=string.ascii_letters) # Generates lettersj
        password += str(object=randomnum) + randomlet # Adds them together
    return password
print(PasswordGen())
