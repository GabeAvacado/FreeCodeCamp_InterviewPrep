def sym(*arg):
    sym_dif = []
    first_list = False
    #Iterate through arguments
    for argument in arg:
        #Determine if it's the first list
        if (len(sym_dif)==0):
            first_list = True
        #Get values of fist argument list to a new list to hold
        for value in argument:
            if (first_list == True):
                sym_dif.append(value)
        #No longer first list, set to False
        if (first_list == True):
            first_list = False
            continue
        #Get symmetric difference
        sym_dif = (set(sym_dif) ^ set(argument))

    return print(list(sym_dif))

sym([1,2,3,3], [5,2,1,4], [5,5,5], [0])