# Find the area of a rectangle (Function)

# Returns it so you can use it later - stores it for later use 
def getAreaRectangle(length, breadth):
    return length * breadth

# Call a subprogram 
print("START")

print(getAreaRectangle(10, 20))

returnedArea = getAreaRectangle(10, 30)
print (returnedArea)

secondReturnedArea = getAreaRectangle(5, 4)

if returnedArea > secondReturnedArea:
    print("First area is bigger! ")