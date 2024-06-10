import math

# Function to compute square root using Newton's method
def logic(n):
    # Initialize answer with a guess (n / 2.0)
    answer = n / 2.0
    
    # Iterate until the guess is accurate enough
    while abs(answer * answer - n) > 0.0001:
        # Refine the guess using Newton's method
        answer = (answer + n / answer) / 2.0
    if answer == 0:
        print("Cannot find 0")
    # Return the final guess as the square root
    return answer

# Prompt the user to enter a number
n = float(input("Enter a number: "))

# Calculate and print the square root of the entered number
print("Square root of", n, "is:", logic(n))
# comments made by AI