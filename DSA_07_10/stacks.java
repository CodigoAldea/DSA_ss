class Node {

    int data;
    Node next;

    // Constructor
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Stack {

    // top points to the top node of the stack
    Node top;

    // Constructor
    Stack() {
        top = null;
    }

    // PUSH
    void push(int data) {

        // Create a new node
        Node newNode = new Node(data);

        // New node points to the current top
        newNode.next = top;

        // New node becomes the new top
        top = newNode;

        System.out.println(data + " pushed into stack");
    }

    // POP
    int pop() {

        // Check if stack is empty
        if (top == null) {
            System.out.println("Stack Underflow");
            return -1;
        }

        // Store the data of top node
        int data = top.data;

        // Move top to the next node
        top = top.next;

        return data;
    }

    // PEEK
    int peek() {

        if (top == null) {
            System.out.println("Stack is empty");
            return -1;
        }

        return top.data;
    }

    // CHECK IF EMPTY
    boolean isEmpty() {

        return top == null;
    }

    // DISPLAY
    void display() {

        if (top == null) {
            System.out.println("Stack is empty");
            return;
        }

        Node current = top;

        System.out.println("Stack:");

        while (current != null) {

            System.out.println(current.data);

            current = current.next;
        }
    }
}

// Main.java

public class Main {

    public static void main(String[] args) {

        // Create Stack
        Stack stack = new Stack();

        // PUSH elements
        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.push(40);

        // Display stack
        stack.display();

        // Peek
        System.out.println("Top element: " + stack.peek());

        // POP
        System.out.println("Popped: " + stack.pop());

        // Display again
        stack.display();

        // Peek again
        System.out.println("Top element: " + stack.peek());

        // Check if empty
        System.out.println("Is stack empty? " + stack.isEmpty());
    }
}