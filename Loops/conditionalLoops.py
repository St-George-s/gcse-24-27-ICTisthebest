# # Question 11
# code = "rzy"
# userInput = input("Enter code: ")
# while code != userInput: 
#     print("Code not accepted. You are wrong.")
#     userInput = input("Enter new code: ")
# print("Code accepted!") 

# # Question 12 - Write a Python program to keep asking for a code until it equals 4003 and print "Code accepted" when the code is correct. 
# code = "4003"
# userInput = input("Enter code: ")
# while code != userInput:
#     print("Code not accepted. You are wrong.")
#     userInput = input("Enter new code: ")
# print("Code accepted!")

# Question 13 - Write a Python program to keep asking for the user's age until it is over 14 and print "Age accepted" once the user enters an age over 14. 
userAge = 14
userInput = input("Enter an age: ")
while int(userInput) <= 14:
    print("Age not accepted. You are too young.")
    userInput = input("Enter new age: ")
print("Age accepted!")

# Question 14 
password = input("What is your password? ")
while len(password) <5:
    password = input("AGAIN, What is your password? ")









