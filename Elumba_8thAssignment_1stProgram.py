# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

answer = input("Would you like to start? y/n: ")

while answer == "y":
    WinningNumberOne = random.randint(0, 9)
    WinningNumberTwo = random.randint(0, 9)
    WinningNumberThree = random.randint(0, 9)
    UserInputOne = int(input("Enter 1st number: "))
    UserInputTwo = int(input("Enter 2nd number: "))
    UserInputThree = int(input("Enter 3rd number: "))

    if UserInputOne == WinningNumberOne and UserInputTwo == WinningNumberTwo and UserInputThree == WinningNumberThree:
        score = 1
    else:
        score = 0

    if score == 1:
        print(f"Winning numbers are: {WinningNumberOne}, {WinningNumberTwo}, {WinningNumberThree}")
        print(f"Your inputs are: {UserInputOne}, {UserInputTwo}, {UserInputThree}.")
        print("Winner!")
        answer = input("Try again y/n: ")
    else:
        print(f"Winning numbers are: {WinningNumberOne}, {WinningNumberTwo}, {WinningNumberThree}")
        print(f"Your inputs are: {UserInputOne}, {UserInputTwo}, {UserInputThree}.")
        print("You loss")
        answer = input("Try again y/n: ")

if answer == "n":
    print("Thank you for participating.")