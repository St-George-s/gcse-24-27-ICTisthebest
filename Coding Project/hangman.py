# Hangman 

# Setting up variables 
word = input("Enter a word: ") 
lives = int(input("Enter number of lives: ")) 
userGuess = "" 
blank = "" 
found = True

# Creating blank  
for i in range (len(word)): 
    blank = blank + "_" 
print(blank) 

# Loop to keep guessing when user has lives 
while lives > 0: 
    
    # Keep asking user for letters when it is not in the word
    while userGuess != blank: 
        userGuess = input("Enter a letter: ") 
        found = False  
        lives = lives - 1  
        print("You have", lives, "lives left") 

        # Loop to check if letter user has guessed is included 
        for i in range(len(word)): 
            if word[i] == userGuess: 
                 found = True  
                 blank = blank [:i] + userGuess + blank[i+1:] 

        # Print blank for user to check correctly guessed letters 
        print(blank) 

    







    
