# Username Validation
count = 0 
username = ""
valid = False

# Loop to give the user 3 chances to enter a username if it is not valid 
while count <3 or valid == False:
    valid = True
    count = count + 1
    username = input("Enter your username: ")

    # Length check
    if len(username) <5: 
        print ("Username is too short! ")
        valid = False
    
    # Checking for spaces
    for i in range(len(username)):
        if username[i] == " ":
            print ("Username has spaces! ")
            valid = False
    
    # Checking for special characters
    for i in range(len(username)):
        if (ord(username[i]) >= 33 and  ord(username[i]) <= 47) or (ord(username[i]) >= 58 and  ord(username[i]) <= 64) or (ord(username[i]) >= 91 and  ord(username[i]) <= 96) or (ord(username[i]) >= 58 and  ord(username[i]) <= 64) or (ord(username[i]) >= 123 and  ord(username[i]) <= 126):
            print ("Username has special characters! ")
            valid = False
    
print("Username is valid! ")
 

    
    
    




































