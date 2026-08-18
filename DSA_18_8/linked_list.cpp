
class Node { 
    public: // this is important because we want to access the data and next pointer of the node from outside the class
    int data;
    Node* next;
    Node(int data) {
        // constructor to initialize the node
        this->data = data;
        this->next = nullptr;
    }
}