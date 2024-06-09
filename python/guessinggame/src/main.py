import random

def game():
    secret_number = random.randint(1, 50)
    attempts = 0
    print("Guessing game")
        
    while True:
        guess = int(input("Enter the guess"))
        attempts += 1
        
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print("you win")
        break
game()