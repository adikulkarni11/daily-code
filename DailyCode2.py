# Given an array of integers, return a new array such that eah element at index i of the new array
# is the product of all numbers in the original array except the one at i.

# Ex if L = [1,2,3,4,5] output should be [120,60,40,30,24]

# Solution without division: make number 1 so that multiplying has no effect in that iteration (check mult)
def productExcept(L):
    finalList = []
    for i, value in enumerate(L):
        tmpList = L

        tmpList[i] = 1
        #print(tmpList)
        mult = 1
        for j in tmpList:
            mult *= j
            #print(mult)
        tmpList[i] = value
        #print("\n"
        finalList.append(mult)

    return finalList

print(productExcept([1,2,3,4,5]))
print(productExcept([3,2,1]))