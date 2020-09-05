# https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/

def findSmallest(arr):

    maxPossible = 1

    for i in range(len(arr)):
        if(arr[i] <= maxPossible):
            maxPossible += arr[i]
        else:
            break
    return maxPossible
            

inputArr = list(map(int, input().split(', ')))
print(findSmallest(inputArr))