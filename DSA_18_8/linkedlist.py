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
    
    def insert_middle(self,data, position):
        # positon of the node before which the new node is to be inserted
        
        new_node = Node(data) # new node 
        
        temp = self.head  # this head is of linkedList and it is pointing to the 1st node.We are using it for the traversal to the required position/node.
        
        for i in range(position - 1):
            temp = temp.next
            
        new_node.next = temp.next
        temp.next = new_node
        
linked_list = LinkedList()
linked_list.insert_start(10)
linked_list.insert_start(20)
linked_list.insert_start(30)