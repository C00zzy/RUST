def dogyears():
    while True:
        try:
            # Prompt the user to input their age and convert it to an integer
            num1 = int(input("What is your age:  "))
            # Calculate the equivalent age in dog years (1 human year = 7 dog years)
            result = num1 * 7
            # Print the result
            print(result)
        # Handle the case where the user interrupts the program (e.g., Ctrl+C)
        except KeyboardInterrupt:
            print("Exiting")
            # Break out of the loop to exit the program
            break

# Call the dogyears function to execute the above logic
dogyears()
#comments made by AI