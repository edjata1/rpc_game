import sys
import random
from enum import Enum

# game function
def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

# playagain = True

# use recursion not: while playagain:

    playerchoice = input("\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissors: \n\n")

    # ERROR HANDLING: handle error 
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")

        # Recursive function 
        return play_rps() 

    # control flow

    # must case playerchoice to int or error
    player = int(playerchoice)

    computerchoice = random.choice("123")

    # must case computerchoice to int or error
    computer = int(computerchoice)

    # using the Enum values and removing the RPS. from output with replace() method
    print("\nplayer: " + str(RPS(player)).replace("RPS.",''))
    print("python: " + str(RPS(computer)).replace("RPS.",'') + "\n")


    if player == 1 and computer == 3:
        print("🥳🎆🏆😏 You won!")
    elif player == 2 and computer == 1:
        print("🥳🎆😘 You won!")
    elif player == 3 and computer == 2:
        print("🥳🎆😘🏆😏 You won!")
    elif player == computer:
        print("😳😲😳 It's a tie game!")
    else:
        print("🐍🐽🐍 Python wins!\n\n")

    print("\nPlay again? ")
    while True:
        playagain = input("\nY for Yes or \nQ to Quit\n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        # recursive call
        return play_rps()
    else:
        print("\n🎆🥳🥳🎆🙌🎆🥳🥳🎆\n")
        print("Thanks for playing!\n")
        # playagain = False
        # or use -> break
        sys.exit("Bye! 👋\n")

# call function 
play_rps()