# https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/

def subArray1(inputArr, inputSum):
    if(inputSum > sum(inputArr)):
        return 0

    minLen = sum(inputArr)
    n = len(inputArr)
    currSum = inputArr[0]
    start = 0
    for i in range(1,n):

        currSum += inputArr[i]

        while(currSum > inputSum):
            if((i - start + 1) < minLen):
                minLen = i - start + 1
            currSum = currSum - inputArr[start]
            if(currSum > inputSum):
                start += 1

    return minLen



def subArray2(inputArr, inputSum):
    if(inputSum > sum(inputArr)):
        return 0
    
    minLen = sum(inputArr)
    n = len(inputArr)
    for i in range(n-1):
        currSum = inputArr[i]
        if(currSum > inputSum):
            return 1
        
        for j in range(i+1, n):
            currSum += inputArr[j]

            if(currSum > inputSum):
                if(j-i+1 < minLen):
                    minLen = j-i+1
                break
    
    return minLen

    
arr = list(map(int, input().split(', ')))
x = int(input())
print(subArray1(arr, x))