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
        
linked_list = LinkedList()
linked_list.insert_start(10)
linked_list.insert_start(20)
linked_list.insert_start(30)