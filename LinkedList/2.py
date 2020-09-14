# https://www.geeksforgeeks.org/sum-of-two-linked-lists/4

from LinkedList import LinkedList as LL

first = LL()
second = LL()
first.push(3) 
first.push(6)
first.push(8)  
first.push(5) 
print("First Linked List:", end=" ")
first.printList() 
second.push(9)
second.push(4) 
second.push(8) 
second.push(2) 
second.push(4) 
second.push(8) 
print("\nSecond Linked List:", end=" ")
second.printList() 

def calculateSize(linkList):
    size = 0
    while(linkList is not None):
        size += 1
        linkList = linkList.next
    return size
firstSize = calculateSize(first.head)
secondSize = calculateSize(second.head)
diff = abs(firstSize - secondSize)
print("Linked List Size: ", firstSize, secondSize, diff)
if(diff != 0):
    if(firstSize < secondSize):
        tempFirst = first.head
        for i in range(diff):
            first.push(0)
    else:
        for i in range(diff):
            second.push(0)
res = LL()
carry = res.addLinkedList2(first.head, second.head)
if(carry > 0):
    res.push(carry)

print("\nAdded Linked List:", end=" ")
res.printList()