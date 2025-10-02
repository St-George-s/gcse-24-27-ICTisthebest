# IF STATEMENTS 
# Question 1 
age = float(input("Enter your age: "))
if age >= 18:
    print("You can watch 18+ movies! ")
else: 
    print("You must not 18+ movies! ")

# Question 2 
age = float(input("Enter your age: "))
if age >= 18:
    print("You can watch 18+ movies! ")
elif age >= 15:
    print("You can watch 15+ movies! ")
else: 
    print("You must not 18+ or 15+ movies! ")

# Question 3 
mood = input("Enter your mood (happy/sad/angry): ")
if mood =="happy":
    print("You are happy! :) ")
elif mood == "sad":
    print("You are sad! :( ")
elif mood == "angry":
    print("You are angry! ")

# Question 4 
genre = input("Enter your favourite genre (fantasy/horror/adventure): ")
if genre =="fantasy":
    print("Lets watch a fantasy movie! ")
elif genre == "horror":
    print("Lets watch a horror movie!")
elif genre == "adventure":
    print("Lets watch an adventure movie! ")

# Question 5 
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
operation = input("Enter an opertaion (add/subtract/multiply/divide): ")
if operation == "multiply":
    print(number1 * number2 )
elif operation == "divide":
    print(number1/number2 )
elif operation == "add":
    print(number1 + number2 )
elif operation == "subtract":
    print(number1 - number2 )

# Comparison and Arithmetic Operators
# Question 1 
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
if number1 == number2:
    print("True")
else: 
    print("False")

# Question 2 
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
if number1 >= number2:
    print(number1)
if number2 >= number1:
    print(number2)

# Question 3 
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
remainder = number1 % number2
print(remainder)

# Question 4 
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(area)

# Question 5 
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
if number1 % number2 == 0:
    print(number1, "is a multiple of", number2)
else: 
    print(number1, "is not a multiple of", number2)






















