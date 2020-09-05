# https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/

def palindromiPartitions(inputStr):
    paritionList = []
    for itr in range(len(inputStr)-1):
        tempList  = []
        for itr2 in range(itr+1, len(inputStr)):
            if(checkPalindrome(inputStr[itr:itr2+1])):
                tempList.append(inputStr[itr:itr2+1])
            else:
                return

        for s in tempList:
            paritionList.append(' '.join(list(s)))

def checkPalindrome(str1):
    if(str1 == str1[::-1]):
        return True
    else:
        return False

inputStr = input()
print(palindromiPartitions(inputStr))