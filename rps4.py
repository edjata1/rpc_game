import sys
import random
from enum import Enum

# global variable 
game_count = 0

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

    # parameters here can have another name
    def decide_winner(player1, computer1):
        if player1 == 1 and computer1 == 3:
            return "🥳🎆🏆😏 You won!"
        elif player1 == 2 and computer1 == 1:
            return "🥳🎆😘 You won!"
        elif player1 == 3 and computer1 == 2:
            return "🥳🎆😘🏆😏 You won!"
        elif player1 == computer1:
            return "😳😲😳 It's a tie game!"
        else:
            return "🐍🐽🐍 Python wins!\n\n"

    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count
    # won't loss count data stored, it's in global scope outside function
    game_count += 1
    print("\nGame count: " + str(game_count))
    

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