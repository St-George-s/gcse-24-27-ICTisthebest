# Linear Search 

def linearSearch(searchValue, searchList):
    # Create an array
    searchValue = "Laya"
    found = False
    index = 0 

    # Conditional loop that stops when 
    # 1. Search value is found
    # 2. The serach is at the end of the list
    while not found and index < len(searchList):
        if searchValue == searchList[index]:
            found = True 
        else:
            index += 1 

# After the loop (unindent)
    if found: 
        print("Found! ")
    else:
        print("Not found! ")

            
# Call out 
linearSearch("Bob", ["Cob", "Rob", "Dob", "Lob"])
linearSearch("Emilia",["Debbie", "Jessie", "Vigdis", "Emilia", "Laya"])
linearSearch(10, [4,3,34,10])