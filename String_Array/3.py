# https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

def countTriplets(arr, sum):
    tripletCount = 0
    n = len(arr)
    arr.sort()
    for index1 in range(n-2):
        index2 = index1+1
        index3 = n-1

        while(index2 < index3):
            if((arr[index1] + arr[index2] + arr[index3]) >= sum):
                index3 -= 1
            else:
                tripletCount += (index3 - index2)
                index2 += 1

    return tripletCount

inputArr = list(map(int,input().split()))
inputSum = int(input())
print(countTriplets(inputArr, inputSum))