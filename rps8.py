import sys
import random
from enum import Enum

# parent function with name parameter and default value
def rps(name='PlayerOne'):

    # variables inside scope of rps function
    game_count = 0
    player_wins = 0
    python_wins = 0

    # 1st nested function inside function
    def play_rps():

        # pulling variable values into play_rps function to modify them
        nonlocal player_wins
        nonlocal python_wins

        # add other nonlocal for name, because it's coming from outer function
        nonlocal name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

    # playagain = True

    # use recursion not: while playagain:
        # using name from nonlocal, need f-string
        playerchoice = input(f"\n{name}, please enter...\n1 for Rock\n2 for Paper\n3 for Scissors: \n\n")

        # ERROR HANDLING: handle error 
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")

            # Recursive function 
            return play_rps() 

        # control flow

        # must case playerchoice to int or error
        player = int(playerchoice)

        computerchoice = random.choice("123")

        # must case computerchoice to int or error
        computer = int(computerchoice)

        # NOTE: still need str{}, because applying it to enum value
        # using the Enum values and removing the RPS. from output with replace() method
        print(f"\n{name}, you chose {str(RPS(player)).replace("RPS.",'').title()}...")

        print(f"python chose {str(RPS(computer)).replace("RPS.",'').title()}....\n")

        # 2nd. nested function, inside of a nested function 
        def decide_winner(player1, computer1):
            
            # to modify values pass down one more level & still access outside decide_winner
            # add, to access player_win and python_wins, inside nested function inside nested function
            nonlocal player_wins
            nonlocal python_wins
            # add other nonlocal for name, because it's coming from outer function
            nonlocal name

            # incrementing variable values, as player and python wins
            if player1 == 1 and computer1 == 3:
                player_wins += 1
                return f"🥳🎆🏆😏 {name}, you won!"
            elif player1 == 2 and computer1 == 1:
                player_wins += 1
                return f"🥳🎆😘 {name}, you  won!"
            elif player1 == 3 and computer1 == 2:
                player_wins += 1
                return f"🥳🎆😘🏆😏 {name}, you  won!"
            elif player1 == computer1:
                return "😳😲😳 It's a tie game!"
            else:
                python_wins += 1
                return f"🥹 😢😭Sorry {name}...., 🐍🐽🐍 Python wins!\n\n"

        print("=" * 30)
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count

        # won't loss count data stored, it's in global scope outside function
        game_count += 1
        print("=" * 30)

        # NOTE: no longer need str() around variables: game_count, player_wins, python_wins
        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython's wins: {python_wins}")
        print(f"=" * 30)

        print(f"\nPlay again, {name}? ")
        while True:
            playagain = input(f"\n{name}, Y for Yes or \nQ to Quit\n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            # recursive call
            return play_rps()
        else:
            print("\n🎆🥳🥳🎆🙌🎆🥳🥳🎆\n")
            print(f"{name}, thanks for playing!\n")
            # playagain = False
            # or use -> break
            sys.exit(f"Bye, bye {name}! 👋👋👋\n")
    # returning function, not calling the function. implementing closure
    return play_rps

# only execute if the rsp is main file 
if __name__ == "__main__":

    # argparse not needed above. used in the action
    # argparse is part of python standard library
    import argparse

    # define parser
    parser = argparse.ArgumentParser(
        # pass in some basic settings argument parser. check Python Standard Library for many other settings
        description="Provides a personalized game experience."
    )

    # pass the arguments to the parser
    parser.add_argument(
        # use at command line as flag for name
        "-n", "--name", metavar="name", # or could dest="firstname" other than name
        required=True, help="The name of the person playing the game."
    )

    # method called on parser
    args = parser.parse_args()

    # NOTE: pass args.name to rps()
    # using closure, created variable "rock_paper_scissors" to hold the play_rps function 
    rock_paper_scissors = rps(args.name)
    # call play function
    rock_paper_scissors()



    # NOTE: must be in folder, also in the command line or terminal:
    # NOTE: on windows: py rps8.py -n "Any_Name_HERE" 

