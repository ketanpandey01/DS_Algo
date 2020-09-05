# geeksforgeeks.org/length-largest-subarray-contiguous-elements-set-1/
from collections import OrderedDict

def findLength(arr):
    n = len(arr) 
    maxCount = 0   
    for index1 in range(n-1):
        maxEle = arr[index1]
        minEle = arr[index1]
        for index2 in range(index1+1, n):
            maxEle = max(maxEle, arr[index2])
            minEle = min(minEle, arr[index2])

            if((maxEle - minEle) == (index2 - index1)):
                maxCount = max(maxCount, (maxEle - minEle)+1)

    return maxCount




inputArr = list(map(int, input().split(', ')))
print(findLength(inputArr))