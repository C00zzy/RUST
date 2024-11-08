import random

def game():
    max_loss_score = -255
    score = 0
    guess_count = 0
    max_guesses = random.randint(1, 100)
    answer = random.randrange(1, 100)
    
    # Pretty header
    print("=====================================")
    print("  Welcome to the Guessing Game!")
    print("=====================================")
    print(f"You have {max_guesses} guesses. Good luck!")
    print("=====================================")
    
    while guess_count < max_guesses:
        guess = int(input("Enter your guess: "))
        guess_count += 1
        
        # Feedback after each guess
        if guess == answer:
            print("\n🎉 You got it! 🎉")
            print(f"The correct answer was {answer}.")
            score += answer
            print(f"You gained score! Score: {score}")
            break
        elif guess < answer:
            print("\n🔻 Too low!")
            print(f"The correct answer was {answer}.")
            score -= answer
            print(f"You lost score! Score: {score}")
        elif guess > answer:
            print("\n🔺 Too high!")
            print(f"The correct answer was {answer}.")
            score -= answer
            print(f"You lost score! Score: {score}")
        
        # End of guesses
        if guess_count == max_guesses:
            print("\nSorry, you lost! The correct answer was:", answer)
            break
        
        # Score penalty check
        if score <= max_loss_score:
            print("\n💥 Your score dropped too low! Resetting score to 0.")
            score = 0

    print("\n=====================================")
    print("  Game Over!")
    print(f"Final Score: {score}")
    print("=====================================")

# Run the game
game()
