# https://www.geeksforgeeks.org/reverse-a-string-without-affecting-special-characters/

import time

def reverseString(inputStr):
    start=0
    end=len(inputStr)-1
    while(start < end):
        if(inputStr[start].isalpha()==False):
            start += 1
        elif(inputStr[end].isalpha()==False):
            end -= 1
        else:
            temp = inputStr[start]
            inputStr[start] = inputStr[end]
            inputStr[end] = temp
            start += 1
            end -= 1
    
    return inputStr


inputStr = input()
startTime = time.time()
print("".join(reverseString(list(inputStr))))
print("Elapsed time", time.time()-startTime)