import random

# function Define the list of words to choose from
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ") 
  
  rand_choice = ["rock", "paper", "scissors"]
  computers_choice = random.choice(rand_choice)
  
  choices = {"computer": computers_choice, "player": player_choice} 
  
  return choices

# Check winner function
def check_win(player, computer):
  print(f"Great game! You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"  
  
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!" 
    else:
      return "Scissors cuts paper! You lose." 
  elif player == "scissors":
    if computer == "rock":
      return "Scissors cuts paper! You win!" 
    else: 
      return "Rock smashes scissors! You lose."
  
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

print("Game Over")