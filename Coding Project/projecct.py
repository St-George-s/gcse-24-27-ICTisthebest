# Username Validation

username = input("Enter your username: ")


has_space = False 
for i in range(len(username)):
    if username[i] == " ":
        has_space = True

has_special = False 
for i in range(len(username)):
    if username[i] == " ":
        has_special = True

for i in range(3):
    if len(username) <5: 
        print ("Username is too short! ")
        username = input("Please enter username again: ")
    
    elif has_space == True:
        print ("Username has spaces! ")
        username = input("Please enter username again: ")

    elif has_special == True:
        print ("Username has special characters! ")
        username = input("Please enter username again: ")
    

    
    
    




































