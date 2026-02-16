# Rock, paper scissors!

import random, os
from art import draw

choices = ["rock", "paper", "scissors"]

def determineWinner(player,opponent):
    # Check if its a tie 
    if player == opponent:
        return("It's a tie game! ")
    
    # Check if player won
    elif ((player == "rock" and opponent == "scissors") or 
         (player == "paper" and opponent == "rock") or 
         (player == "scissors" and opponent == "paper") ):
        return("You win congratulations! ")
    
    # Check if player lost 
    else: 
        return("You lost! Oh no! ")

playing, invalid = True, False

# Loop to make sure players can enter choice if they want to play
while playing: 
    # If statement to check if player has not written random answers
    if not invalid:
        print("Rock, paper or scissors? ")
    else:
        print("Invalid input! Please choose rock, paper or scissors: ")
        invalid = False
    print("Or enter q to quit ")

    # Get players selection and convert upper case letters to lowercase and remove white space
    playerChoice =  input("Enter your choice: ").lower().strip()

    # Generate random choice for the computer 
    opponentChoice = random.choice(choices)

    # If statement to check if player has made a valid entry
    if playerChoice in choices: 
        print("You choose: "+ playerChoice+ draw(playerChoice))
        print("Your opponent choose:"+ opponentChoice+ draw(opponentChoice))
        print(determineWinner(playerChoice, opponentChoice))
    
    # End loop if player wants to leave 
    elif playerChoice == "q":
        playing = False
    
    else:
        invalid = True 

    # The iteration of the game is done, ask to play again
    if playing and not invalid:
        replay = input("Wanna play again?\nType \"yes\" to replay\nEnter anything else to end game\n").lower().strip()
        print()
        playing = replay == "yes"

        # Clear the system
        os.system("cls" if os.name == "nt" else "clear")

print("Thanks for playing! Hope you enjoyed! ")
