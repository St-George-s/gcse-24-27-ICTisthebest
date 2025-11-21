# Question `1a
import random 

myRandomNumber = random.randint(1, 3)
print(myRandomNumber)

# Question 1b
import random 

myRandomNumber = random.randint(1, 3)
print(myRandomNumber)
if myRandomNumber == 1:
    print("Go walk 10 km!")
elif myRandomNumber == 2:
    print("Go run 5km!")
elif myRandomNumber == 3:
    print("Go swim 1km")

# Question 2
counta = 0 
while counta <3:
    word = input("Enter a desired word: ")
    for letter in word:
        if letter == "a" or letter == "A":
            counta = counta + 1
print("This word has", counta, "A's in it")

# Question 3a 
trainingdata = ["2", "New Trent Park", "True", "12.7"] 
with open ("allsessions.txt", "w") as file:
    file.write("Number of goals scored: " + trainingdata[0] + "\n")
    file.write("Training venue: " + trainingdata[1] + "\n") 
    file.write("Session completed: " + trainingdata[2] + "\n") 
    file.write("Best sprint time: " + trainingdata[3] + "\n") 

# Question 3b 
trainingdata = ["2", "New Trent Park", "True", "12.7"] 
print(trainingdata[1])

# Question 4 
numberX = float(input("Input a number: "))
numberY = float(input("Input a number: "))
remainder = numberX % numberY 
wholeNumber = numberX // numberY
print("Whole number: " + str(wholeNumber))   
print("Remainder: " + str(remainder))  



