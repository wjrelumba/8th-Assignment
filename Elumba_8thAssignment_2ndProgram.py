# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random
answer = "y"
RandomNumber = random.randint(0, 100)

while answer == "y":
    UserInput = int(input("Enter your guess: "))
    if UserInput == RandomNumber:
        print("You are correct!")
        break
    elif UserInput > RandomNumber:
        print("Greater than")
        answer = "n"
        answer = "y"
    elif UserInput < RandomNumber:
        print("Less than")
        answer = "n"
        answer = "y"