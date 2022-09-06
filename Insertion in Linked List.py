class Node:

    def __init__ (self, data):
        self.data = data 
        self.next = None 
 
class LinkedList: 
    def __init__ (self): 
        self.head = None 
 
    def insert (self, data):
        new_node = Node (data) 
        new_node.next = self.head 
  
        #changing the head to freshly entered node
        self.head = new_node 
 
    def display (self):
        temp = self.head 
        while temp:     
            print (temp.data, end = " ") 
            temp = temp.next 
        print ("\n") 
 
    def delete_node (self, pos):
        temp = self.head 
        previous = None 
    
        #if the head node itself needs to be deleted
        size = self.calcSize () 
 
        if pos <1 or pos > size:
            print ("Enter valid position, pos: {0}, size: {1}".format (pos, size)) 
            return 
 
        if pos== 1:
            #Case 1 head becomes 30
	        self.head = temp.next
            #changing head to next in the list
	        print("Value deleted: ", temp.data) 
            return
 
        #run until we find the value to be deleted in the list
	    for i in range (1, pos):
            #store previous link node as we need to change its next val
	        previous = temp 
            temp = temp.next 
            pos -= 1 
 
        #Case 2: (24)->next = 16 (as 20->next = 16)
        #Case 3: (16)->next = NULL (as 12->next = NULL)
        previous.next = temp.next 
        print ("Value deleted: ", temp.data) 
 
    def calcSize (self):
        size = 0 
	    node = self.head 
	  
        while node is not None:
            node = node.next 
            size += 1 

        return size 
 
#Drive Code
ll = LinkedList () 
	    
ll.insert (12) 
ll.insert (16) 
ll.insert (20) 
ll.insert (24) 
ll.insert (30) 
ll.insert (22) 
	    
ll.display () 
	    
ll.delete_node (1) 
ll.display () 
	    
ll.delete_node (3) 
ll.display () 
	    
ll.delete_node (4) 
ll.display () 
	    
ll.delete_node (-2) 
ll.delete_node (10) 
 
ll.display () 
