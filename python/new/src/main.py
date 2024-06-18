import time

def stopwatch():
    duration = input("What time:  ")

    try:
        duration = int(duration)
        print(f"stop watch running for {duration} seconds...")
        time.sleep(duration)
        print("Time's up")
    except ValueError:
        print("Invalid")
stopwatch()