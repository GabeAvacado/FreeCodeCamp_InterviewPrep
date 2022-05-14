def checkInventory(arr1, item):
    #Iterate through current inventory list
    for list in arr1:
        #If item already in list, return current info of item
        if (item in list):
            found_item = list
            #remove the current item info
            arr1.remove(list)
            return found_item

def updateInventory(arr1, arr2):
    #Iterate through new inventory list
    for list in arr2:
        #Initalize empty list to keep track of current item
        current = []
        #Get the item names
        for i in range(len(list)):
            if (i == 1):
                #Check if item in current inventory
                current = checkInventory(arr1, list[i])
        #If item was in current invtory, update the quantity
        if (current != None):
            list[0] = list[0] + current[0]

    #Append the remaining items from current inventory list to new inventory list
    for list in arr1:
        arr2.append(list)

    #sort list base on item names
    arr2.sort(key = lambda x: x[1])

    return print(arr2)

                


# Example inventory lists
curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]

updateInventory(curInv, newInv)