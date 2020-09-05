# https://www.geeksforgeeks.org/reverse-a-string-without-affecting-special-characters/

import time

def reverseString(inputStr):
    strWithouSpecial = ""
    for ch in inputStr:
        if(ch.isalpha()):
            strWithouSpecial += ch
    
    revStr = strWithouSpecial[::-1]
    outputStr = ""
    j = 0
    for index in range(len(inputStr)):
        if(inputStr[index].isalpha()):
            outputStr += revStr[j]
            j += 1
        else:
            outputStr += inputStr[index]

    return outputStr

inputStr = input()
startTime = time.time()
print(reverseString(inputStr))
print("Elapsed time", time.time()-startTime)