# https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/

def convertToZigZag(arr):
    n = len(arr)
    for index in range(n-1):
        # if position is even
        if((index+1)%2==0):
            if(arr[index] < arr[index+1]):
                arr[index], arr[index+1] = arr[index+1], arr[index]
        # if position is odd
        else: 
            if(arr[index] > arr[index+1]):
                arr[index], arr[index+1] = arr[index+1], arr[index]
    
    return arr

inputArr = list(map(int, input().split()))
print(*convertToZigZag(inputArr))