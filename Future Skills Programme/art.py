def draw (choice): 
    # Checks if player choose rock 
    if choice == "rock":
        return("""    
         _______
        ---'   ____)
               (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    
    # Checks if player choose paper 
    elif choice == "paper":
        return("""
            _______
        ---'    ___)___
                   ______)
                   _______)
                  _______)
        ---.__________)
        """)
    
    # Checks if player choose scissors
    elif choice == "scissors":
        return("""
            _______
         ---'   ___)___
                    ______)
                 __________)
              (.____)
        ---.__(___)
        """)