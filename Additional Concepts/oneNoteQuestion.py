# Question 1 
userInput = (input("Enter a character: "))
print(userInput[0])
print(userInput[-1])
 
# Question 2 
myString = (input("Enter a character: "))
reverseString = ""
for character in myString:
    reverseString = character + reverseString
print(reverseString)

# Question 6 
import random 

myRandomNumber = random.randint(1, 6)
print(myRandomNumber)

# Question 7 
import random 

myRandomNumber1 = random.randint(1, 6)
myRandomNumber2 = random.randint(1, 6)

print(str(myRandomNumber1) + "+" + str(myRandomNumber2) + "=")
print(str(myRandomNumber1 + myRandomNumber2))
