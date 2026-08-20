class Node : 
    def __init__(self,data) : 
        self.data = data  # this is for the data 
        self.next = None  # this is for the refrence or the pointer 
        

class LinkedList : 
    def __init__(self) : 
        self.head = None # this is the 1st arrow that points to the head of the linked list.
        
    def insert_start(self,data) : 
        new_node = Node(data) # creating a new node 
        new_node.next = self.head # pointing the new node to the head
        self.head = new_node # pointing the head to the new node
        
    def insert_middle(self, data, position) : 
        new_node = Node(data) # creating a new node 
        if position == 0 : 
            self.insert_start(data) # if the position is 0 then we will insert at the start
            return
        current = self.head # pointing the current to the head
        for i in range(position - 1) : 
            if current is None : 
                print("Position out of bounds") # if the position is out of bounds
                return
            current = current.next # pointing the current to the next node
        new_node.next = current.next # pointing the new node to the next node
        current.next = new_node # pointing the current to the new node
    
        
linked_list = LinkedList()
linked_list.insert_start(10)
linked_list.insert_start(20)
linked_list.insert_start(30)

