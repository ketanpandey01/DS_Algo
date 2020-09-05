# geeksforgeeks.org/length-largest-subarray-contiguous-elements-set-1/
from collections import OrderedDict

def findLength(arr):
    n = len(arr)
    maxEle = max(arr) if arr else 0
    oDict = OrderedDict()
    for i in range(0, maxEle+1):
        if(i not in oDict.keys()):
            if(i not in arr):
                oDict[i] = 0
            else:
                oDict[i] = 1
    
    maxCount = 0
    tempCount = 0
    c = 0
    for value in oDict.values():
        c+=1
        if(value==1):
            tempCount += 1
        elif(tempCount > maxCount):
            maxCount = tempCount
            tempCount = 0
        else:
            tempCount = 0
    
    if(tempCount > maxCount):
        maxCount = tempCount
    
    return maxCount



inputArr = list(map(int, input().split(', ')))
print(findLength(inputArr))