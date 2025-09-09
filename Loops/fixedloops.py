# Example 
for counter in range(10):
    print(counter)

# Fixed Loops (Count Contolled) 
# Question 1 - Write a Python program to print your name 10 times
for counter in range(10):
    print("Liyana")

# Question 2 - 	1. Ask for your name and print your name 1000 times
name = input("Enter your name: ")
for counter in range(1000):
    print(name)

# Question 3 - Ask for your name and print "Hello" then your name 1000 times
name = input("Enter your name: ")
for counter in range(1000):
    print("Hello", name) 

# Question 4 - Write a Python program to print the answers to the 8 times table from 1 to 12
for counter in range(1, 13): 
    print(counter * 8)

# Question 5 - Write a Python program to print the answers to the 8 times table from 1 to 1000
for counter in range(1, 1001):
    print(counter * 8)

# Question 6 - 	1. Calculate the 7 times table up to 12 and print "7 x number = answer" each time
for counter in range(1, 13):
    print(counter, "x 7", "=", counter * 7)

# Question 7 - Write a Python program to ask the user to input the age of 10 people and print each age
for counter in range (10):
    age = input("Enter an age: ")
    print(age)

# Question 8 - Ask the user for the age of 10 people and print the age of each person in ten yearsd time
for counter in range (10):
    age = input("Enter an age: ")
    newAge = int(age) + 10
    print(newAge)

# Question 9 - Ask the user the age of 10 people, add up all the ages and print the total ages
total = 0 
for counter in range(10):
    age = int(input("Enter an age:"))
    total = total + age 
    print(total)

# Question 10 - Write a Python program to output the 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12 times tables from 1 to 12
for counter1 in range(1,1000):
    print("")
    print(counter1, "Time table")
    for counter2 in range(1,13):
        print(counter1, "x", counter2, "=", counter1 * counter2)

    


   





