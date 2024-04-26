import sys
import random
from enum import Enum

# parent function
def rps():

    # variables inside scope of rps function
    game_count = 0
    player_wins = 0
    python_wins = 0

    # 1st nested function inside function
    def play_rps():
        # pulling variable values into play_rps function to modify them
        nonlocal player_wins
        nonlocal python_wins

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

        # 2nd. nested function, inside of a nested function 
        def decide_winner(player1, computer1):
            
            # to modify values pass down one more level & still access outside decide_winner
            # add, to access player_win and python_wins, inside nested function inside nested function
            nonlocal player_wins
            nonlocal python_wins

            # incrementing variable values, as player and python wins
            if player1 == 1 and computer1 == 3:
                player_wins += 1
                return "🥳🎆🏆😏 You won!"
            elif player1 == 2 and computer1 == 1:
                player_wins += 1
                return "🥳🎆😘 You won!"
            elif player1 == 3 and computer1 == 2:
                player_wins += 1
                return "🥳🎆😘🏆😏 You won!"
            elif player1 == computer1:
                return "😳😲😳 It's a tie game!"
            else:
                python_wins += 1
                return "🐍🐽🐍 Python wins!\n\n"

        print("=" * 30)
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        # won't loss count data stored, it's in global scope outside function
        game_count += 1
        print("=" * 30)
        print("\nGame count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))
        print("=" * 30)

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
    # returning function, not calling the function. implementing closure
    return play_rps

# create variable "play" to hold the play_rps function 
play = rps()

# call play function
play()