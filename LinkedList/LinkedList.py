class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert node so that linked list remain sorted(ascending order)
    def sortedInsert(self, newNode):
        if((self.head is None) or (newNode.data <= self.head.data)):
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            while((current.next is not None) and newNode.data > current.next.data):
                current = current.next

            newNode.next = current.next
            current.next = newNode

    # Insert node at the beginning of the linked list
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, data):
        temp = self.head
        prev = self.head
        # If node to delete is the first node or the only node
        if(temp.data == data):
            self.head = temp.next
            temp.next = None
            return
        else:
            while(temp.next != None and temp.data != data):
                prev = temp
                temp = temp.next
            # If node to delete is not found
            if(temp.data != data):
                print('Node not found')
            else:
                prev.next = temp.next
                temp.next = None

    def printList(self):
        current = self.head
        while(current):
            print(current.data, end=" ")
            current = current.next

    def addLinkedList(self, first, second):
        temp = None
        prev = None
        carry = 0
        while(first is not None or second is not None):
            fData = first.data if first is not None else 0
            sData = second.data if second is not None else 0
            nodeSum = fData + sData + carry
            carry = 1 if nodeSum >= 10 else 0
            nodeSum = nodeSum % 10 if nodeSum >= 10 else nodeSum

            temp = Node(nodeSum)
            if(self.head is None):
                self.head = temp
            else:
                prev.next = temp
            prev = temp

            if(first is not None):
                first = first.next
            if(second is not None):
                second = second.next

        if(carry > 0):
            temp.next = Node(carry)

    def addLinkedList2(self, first, second):
        if(first.next is None and second.next is None):
            nodeSum = first.data + second.data
            carry = 1 if nodeSum >= 10 else 0
            nodeSum = nodeSum%10 if nodeSum >= 10 else nodeSum
            self.push(nodeSum)
            return carry

        carry = self.addLinkedList2(first.next, second.next)
        nodeSum = first.data + second.data + carry
        carry = 1 if nodeSum >= 10 else 0
        nodeSum = nodeSum%10 if nodeSum >= 10 else nodeSum
        self.push(nodeSum)

        return carry
        
        

# llist = LinkedList() 
# llist.push(3) 
# llist.push(2) 
# llist.push(6) 
# llist.push(5) 
# llist.push(11) 
# llist.push(10) 
# llist.push(15) 
# llist.push(12) 

# print("Given Linked List: ", end = ' ') 
# llist.printList() 
# print("\n\nDeleting node 10:") 
# llist.deleteNode(10) 
# print("Modified Linked List: ", end = ' ') 
# llist.printList() 
# print("\n\nDeleting first node") 
# llist.deleteNode(12) 
# print("Modified Linked List: ", end = ' ') 
# llist.printList() 
# print("\n\nDeleting last node") 
# llist.deleteNode(3) 
# print("Modified Linked List: ", end = ' ') 
# llist.printList() 

# llist = LinkedList() 
# new_node = Node(5) 
# llist.sortedInsert(new_node)
# new_node = Node(10) 
# llist.sortedInsert(new_node) 
# new_node = Node(7) 
# llist.sortedInsert(new_node)    
# new_node = Node(3) 
# llist.sortedInsert(new_node) 
# new_node = Node(1) 
# llist.sortedInsert(new_node) 
# new_node = Node(9) 
# llist.sortedInsert(new_node)
# print("Sorted Linked List")
# llist.printList()
