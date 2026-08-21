class Node :
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_start(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return 
        
        new_node.next = self.head
        
        self.head.prev = new_node
        
        self.head = new_node
        
    def insertion_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return 
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        
    def insert_mid(self, data, position):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return 
        
        temp = self.head # node1
        
        for i in range(position-1): 
            temp = temp.next
            
        new_node.next =  temp.next
        temp.next = new_node
        new_node.prev = temp
        