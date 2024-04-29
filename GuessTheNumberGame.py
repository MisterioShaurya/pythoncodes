import random

randomnu = random.randint(1, 100)
i = 0  # Initialize the variable to count guesses

while True:
    guess = int(input("Enter a number between 1 to 100: "))
    i += 1  # Increment the guess count with each iteration

    if guess < randomnu:
        print("Higher number please.")
    elif guess > randomnu:
        print("Lower number please.")
    else:
        print(f"YAY! You won the game in {i} guesses")
        break  # Exit the loop when the correct number is guessed
