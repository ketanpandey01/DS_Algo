# https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/

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

res = LL()
res.addLinkedList(first.head, second.head)
print("\nAdded Linked List:", end=" ")
res.printList()