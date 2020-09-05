def isPalindrome(string: str, 
                 low: int, high: int): 
    while low < high: 
        if string[low] != string[high]: 
            return False
        low += 1
        high -= 1
    return True

def allPalPartUtil(allPart: list, currPart: list,  
                   start: int, n: int, string: str): 
  
    # If 'start' has reached len 
    if start >= n: 
          
        # In Python list are passed by reference 
        # that is why it is needed to copy first 
        # and then append 
        x = currPart.copy() 
  
        allPart.append(x) 
        return
  
    # Pick all possible ending points for substrings 
    for i in range(start, n): 
  
        # If substring str[start..i] is palindrome 
        if isPalindrome(string, start, i): 
  
            # Add the substring to result 
            currPart.append(string[start:i + 1]) 
  
            # Recur for remaining remaining substring 
            allPalPartUtil(allPart, currPart,  
                            i + 1, n, string) 
  
            # Remove substring str[start..i]  
            # from current partition 
            currPart.pop() 
  
# Function to print all possible  
# palindromic partitions of str.  
# It mainly creates vectors and  
# calls allPalPartUtil() 
def allPalPartitions(string: str): 
  
    n = len(string) 
  
    # To Store all palindromic partitions 
    allPart = [] 
  
    # To store current palindromic partition 
    currPart = [] 
  
    # Call recursive function to generate  
    # all partitions and store in allPart 
    allPalPartUtil(allPart, currPart, 0, n, string) 
  
    # Print all partitions generated by above call 
    for i in range(len(allPart)): 
        for j in range(len(allPart[i])): 
            print(allPart[i][j], end = " ") 
        print() 

if __name__ == "__main__": 
    string = "nitin"
    allPalPartitions(string) 