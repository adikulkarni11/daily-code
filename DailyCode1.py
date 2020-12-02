def kSum(List, k):

    # Creates pos and value for each in List
    for pos, value in enumerate(List[:-1]): #Dont need to check last value (to save time)
        if k < value:
            pass
        complement = k - value
        if complement in List[pos:]: 
            print("Numbers found:" ,value, "+" ,  complement, "=" , k, "\n\n")
        
kSum([10,15,3,7],17)
