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

