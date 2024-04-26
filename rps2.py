import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:

    playerchoice = input("\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissors: \n\n")

    # control flow

    # must case playerchoice to int or error
    player = int(playerchoice)

    # [ctrl] + [d] to select all after selecting one player to change name
    if player < 1 or player > 3:
        sys.exit("You must select 1, 2, or 3.")

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

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit\n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎆🥳🥳🎆🙌🎆🥳🥳🎆\n")
        print("Thanks for playing!\n")
        playagain = False
        # or use -> break

sys.exit("Bye! 👋\n")