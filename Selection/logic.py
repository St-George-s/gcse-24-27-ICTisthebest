# The Weather - Class Example 
weather = input("Enter weather (sunny/rainy): ")
timeOfDay = input("Enter time (day/night): ")

if weather == "sunny" and timeOfDay == "day":
    print("No umbrella needed. Enjoy your day! ")
elif weather == "rain" and (timeOfDay == "day" or timeOfDay == "night"):
    print("Take an umbrella! ")


# LOGIC
# Question 1
weather = input("Enter weather (sunny/rainy): ")
temperature = float(input("Enter a tempertaure: "))
if weather == "sunny" and temperature > 15:
    print("It's sunny and the tempertaure is over 15! Go outside! ")

else:
    print("Stay inside! ")

# Question 2 
weather = input("Enter weather (sunny/rainy): ")
temperature = float(input("Enter a tempertaure: "))
if weather == "rainy" or temperature > 15:
    print("Do not go outside! ")

else:
    print("Go touch grass! ")

# Question 3 
apples = float(input("Enter number of apples: "))
if apples <10:
    print("Terrible Harvest! ")

else:
    print ("Great Harvest! ")

# Question 4 
age = float(input("Enter an age: "))
driversLicense = input("Do you have a driver license (yes/no): ")
if age <18 and driversLicense == "yes":
    print("You may go drive! ")
elif age >18 and driversLicense == "yes":
    print ("You can't drive! ")
else:
    print("Go get a license! ")

# Question 5
speedOfCar = float(input("Enter your car speed: "))
weather = input("Is it raining (yes/no)?: ")
if speedOfCar >60 or weather == "yes":
    print("Drive more safely and slowly! ")

else:
    print ("Have a safe journey! ")


# Question 6 
hoursRevised = float(input("Enter how many hours you revised: "))
prepared = input("Do you feel prepared (yes/no): ")
if hoursRevised  >5 and prepared == "yes":
    print ("You are ready! ")
elif hoursRevised >5 and prepared == "no":
    print("Don't worry! You can do this! ")
else:
    print("GO REVISE! ")

# Question 7 
assignmentsCompleted = float(input("How many assigments have you completed? "))
assigmentsToDo = float(input("How many assgiments do you need to do? "))
if assignmentsCompleted >5 and assigmentsToDo <2: 
    print("Great job! You can take a break!")
else: 
    print("Go do your assigments! ")

# Question 8 
savings = float(input("Enter your savings: "))
item = float(input("Enter your desired item price: "))
if savings >= item:
    print("You may buy the item! ")
else: 
    print("You do not have enough ")

# Question 9 
weather = input("What is the weather (sunny/rainy)? ")
dayOfTheWeek = input("What is the day of the week (weekday/weekend)? ")
if weather == "sunny" and dayOfTheWeek == "weekend":
    print("You may go outside! Enjoy your day! ")
elif weather == "rainy" and dayOfTheWeek == "weekend":
    print("Lets have a movie day! ")
else: 
    print("Go do your homework! ")

