# # Linear Search 

# # Create an array
# names = ["Debbie", "Jessie", "Vigdis", "Emilia", "Laya"]
# searchValue = "Laya"
# found = False
# index = 0 

# # Conditional loop that stops when 
# # 1. Search value is found
# # 2. The serach is at the end of the list
# while not found and index < len(names):
#     if searchValue == names[index]:
#         found = True 
#     else:
#         index += 1 

# # After the loop (unindent)
# if found: 
#     print("Found! ")
# else:
#     print("Not found! ")

# STARTER
def linearSearch(searchValue, searchList, names):
    found = False 
    index = 0 
    
    while not found and index < len(searchList):
        if searchValue == searchList[index]:
            found = True 
        else:
            index += 1 

    if found: 
        print("Found at ", index)
    else:
        print("Not found! ")

linearSearch(False, [True, True, False], ["Jessie," "Debbie", "Maggie"])


