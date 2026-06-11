# Procedure with one parameter name - does not return name
def printName(name):
    print(name)

# Function with one parameter name - returns name
def printNameFunc(name):
    return name 

# Call the procedure 
printName("Liyana")

# Call the function and print returned value
print(printNameFunc("Vigdis"))

# Call the function and store retured value in a variable
returnedName = printNameFunc("Alina")
print(returnedName)

# Question 4 
def sphere_volume(radius):
    volume = 4/3 * 3.14 * radius**3
    return volume 

answer = sphere_volume(5)
print(round(answer,2))

# Question 6 
def linear_search(data_list,target):
    found = False
    index = 0 

    while not found and index <len(data_list):
        if data_list == target[index]:
            found = True 
        else:
            index += 1

    if found: 
        print("Found at", index)

    else:
        print("Not found!")
    
answer = linear_search ([3, 8, 2, 10, 7], 10)
print(answer)

