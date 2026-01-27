usernameLength = 0
specialCount = 0
specialLetters = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "@", "~", "#", ":", "<", ">", "?", "'", ";", ",", ".", "¬", "`"]
username = input("Enter your username: ")

has_space = False 
for i in range(len(username)):
    if username[i] == " ":
        has_space = True

while has_space == True: 
     print ("Please delete spaces in your username! ")
     username = input("Please enter username again: ")























