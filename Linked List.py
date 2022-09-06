#Note Classes are are mutable data type in python 
class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None 
 
class LinkedList: 
    def __init__ (self): 
        self.head = None 
 
    def insertStart(self, data):
        new_node = Node (data) 
        new_node.next = self.head 
  
        #changing the head to freshly entered node
        self.head = new_node 
 
    def insertLast(self, data):
        new_node = Node (data) 
  
        new_node.next = None 
 
        #need this if there is no node present in linked list at all
        if self.head is None:
            self.head = new_node 
            return 
 
        temp = self.head 
 
        while temp.next is not None: 
            temp = temp.next 
 
        temp.next = new_node 
    
    def insertPosition (self, pos, data):
        size = self.calcSize () # will calculate the size of the linked list
        
        if pos == 0:
          self.insertStart(data)
          
        if pos<0 or size<pos:
            print ("Can't insert", pos," is not valid position") 
        else:
            temp = self.head 
            new_node = Node (data) 

        for i in range(1, pos): 
            temp = temp.next 
            pos -= 1 
 
        new_node.next = temp.next 
        temp.next = new_node 

    def display(self) :
        temp = self.head 
	    while temp : 
            print (temp.data, end = " ") 
            temp = temp.next 
 
    def calcSize(self):
        size = 0 
        node =self.head 

        while node is not None:
            node = node.next 
            size +=1 
        return size 
 
#Drive Code
ll = LinkedList() 

ll.insertStart(12) 
ll.insertStart(16) 
ll.insertStart(20) 
	      
ll.insertLast(10) 
ll.insertLast(14) 
ll.insertLast(18) 
ll.insertLast(11) 
 
#Inserts after 3rd position
ll.insertPosition(3, 25) 
 
ll.display() 
