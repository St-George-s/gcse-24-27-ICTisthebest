usernameLength = 0
specialCount = 0
specialLetters = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "@", "~", "#", ":", "<", ">", "?", "'", ";", ",", ".", "¬", "`"]
username = input("Enter your username: ")

while len(username) <5: 
    print ("Please make username at least 5 characters long! ")
    username = input("Please enter username again: ")

has_space = False 
for i in range(len(username)):
    if username[i] == " ":
        has_space = True

while has_space == True: 
     print ("Please delete spaces in your username! ")
     username = input("Please enter username again: ")























