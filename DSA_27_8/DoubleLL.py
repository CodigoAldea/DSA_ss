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
    
    
    def delete_start(self):
        if self.head is None:
            print("Enpty List")
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        self.head = self.head.next
        self.head.prev = None
        
    def delete_end(self):
        if self.head is None:
            print("Enpty List")
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        self.tail = self.tail.prev
        self.tail.next = None
        
    def delete_mid(self, positon):
        if self.head is None:
            print("Enpty List")
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        temp = self.head
        
        for i in range(positon):
            temp = temp.next
            
        temp.prev.next = temp.next
        
        if temp.next is not None:
            temp.next.prev = temp.prev
            
        if temp == self.tail:
            self.tail = temp.prev
            
    def display_lr(self):
        temp = self.head
        while temp:
            print(temp.data, end= "⇄")
            temp.next
        print("None")
        
    def display_rl(self):
        temp = self.tail
        
        while temp:
            print(temp.data, end= "⇄")
            temp.prev

        print("None")
        
        
# for(Node temp = head; temp != null; temp=temp.next)