# # Question `1a
# import random 

# myRandomNumber = random.randint(1, 3)
# print(myRandomNumber)

# # Question 1b
# import random 

# myRandomNumber = random.randint(1, 3)
# print(myRandomNumber)
# if myRandomNumber == 1:
#     print("Go walk 10 km!")
# elif myRandomNumber == 2:
#     print("Go run 5km!")
# elif myRandomNumber == 3:
#     print("Go swim 1km")

# Question 2
counta = 0 
word = input("Enter a desired word: ")
while counta <3:
    counta = 0

for letter in word:
        if letter == "a" or letter == "A":
            counta = counta + 1
print("This word has", counta, "a in it")



