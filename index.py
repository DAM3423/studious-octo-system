import sys
import random

entries = ["Rock", "Paper", "Scissors"]

computerAnswer = random.choice(entries)
userInput = input("Rock, Paper or Scissors?")


if userInput not in entries:
    print("Pick an actual answer you dummy")
    sys.exit()


if userInput == computerAnswer:
    print("You picked the same")
elif userInput == "Rock":
    if computerAnswer == "Paper":
        print("Computer picked Paper, you lose.")
    else:
        print("Computer picked Rock, you win!")
elif userInput == "Paper":
    if computerAnswer == "Scissors":
        print("Computer picked Scissors, you lose.")
    else:
        print("Computer picked Rock, you win!")
elif userInput == "Scissors":
    if computerAnswer == "Rock":
        print("Computer picked Rock, you lose.")
    else:
        print("Computer picked Paper, you win!")
