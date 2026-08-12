#include <iostream>
using namespace std;

class Node {
public:
    int data;       // stores the data
    Node* next;     // pointer to the next node

    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }
};

class LinkedList {
public:
    Node* head;     // head points to the first node

    LinkedList() {
        this->head = nullptr;
    }

    void insert(int data) {
        Node* newNode = new Node(data); // creating a new node

        newNode->next = head;            // new node points to old head

        head = newNode;                 // head now points to new node
    }
};

int main() {

    LinkedList linkedList;

    linkedList.insert(1);
    linkedList.insert(2);
    linkedList.insert(3);

    return 0;
}