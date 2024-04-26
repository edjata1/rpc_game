import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print()
playerchoice = input("Enter...\n1 for Rock\n2 for Paper\n3 for Scissors: \n\n")

# control flow

# must case playerchoice to int or error
player = int(playerchoice)

# [ctrl] + [d] to select all after selecting one player to change name
if player < 1 or player > 3:
    sys.exit("You must select 1, 2, or 3.")

computerchoice = random.choice("123")

# must case computerchoice to int or error
computer = int(computerchoice)

print()

# using the Enum values and removing the RPS. from output with replace() method
print("player: " + str(RPS(player)).replace("RPS.",''))
print("python: " + str(RPS(computer)).replace("RPS.",''))

print() 

if player == 1 and computer == 3:
    print("🥳🎆🏆😏 You won!")
elif player == 2 and computer == 1:
    print("🥳🎆😘 You won!")
elif player == 3 and computer == 2:
    print("🥳🎆😘🏆😏 You won!")
elif player == computer:
    print("😳😲😳 It's a tie game!")
else:
    print("🐍🐽🐍 Python wins!")

print()
print()