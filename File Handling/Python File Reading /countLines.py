with open("/workspaces/gcse-24-27-ICTisthebest/holidays.txt", "r") as file:
    counter = 0 
    for line in file:
        counter = counter + 1
    print("There are", counter, "lines")