public class PriorityQueue {

    static class Node {

        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    Node head;

    // Priority is maintained separately
    int[] priorities;

    int size;
    int capacity;

    PriorityQueue(int capacity) { // capacity is the priorities of the node 

        this.capacity = capacity;

        head = null;

        priorities = new int[capacity];

        size = 0;
    }

    void enqueue(int data, int priority) {

        if (size == capacity) {
            System.out.println("Priority Queue is full");
            return;
        }

        Node newNode = new Node(data);

        // Insert at beginning
        newNode.next = head;
        head = newNode;

        // Store priority separately
        priorities[size] = priority;

        size++;
    }

    int getHighestPriorityIndex() {

        if (size == 0) {
            return -1;
        }

        int highestIndex = 0;

        for (int i = 1; i < size; i++) {

            if (priorities[i] > priorities[highestIndex]) {
                highestIndex = i;
            }
        }

        return highestIndex;
    }

    int dequeue() {

        if (head == null) {
            System.out.println("Priority Queue is empty");
            return -1;
        }

        int highestIndex = getHighestPriorityIndex();

        Node current = head;
        Node previous = null;

        for (int i = 0; i < highestIndex; i++) {

            previous = current;
            current = current.next;
        }

        int removedData = current.data;


        // Remove node from linked list
        if (previous == null) {

            // Removing head
            head = current.next;

        } else {

            previous.next = current.next;
        }


        // Shift priorities
        for (int i = highestIndex; i < size - 1; i++) {

            priorities[i] = priorities[i + 1];
        }

        size--;

        return removedData;
    }

    int peek() {

        if (head == null) {
            System.out.println("Priority Queue is empty");
            return -1;
        }

        int highestIndex = getHighestPriorityIndex();

        Node current = head;

        for (int i = 0; i < highestIndex; i++) {
            current = current.next;
        }

        return current.data;
    }

    void display() {

        if (head == null) {
            System.out.println("Priority Queue is empty");
            return;
        }

        Node current = head;

        int index = 0;

        System.out.println("Data\tPriority");

        while (current != null) {

            System.out.println(
                current.data + "\t" + priorities[index]
            );

            current = current.next;

            index++;
        }
    }


    // ==========================================
    // MAIN
    // ==========================================

    public static void main(String[] args) {

        PriorityQueue pq = new PriorityQueue(5);


        // data, priority
        pq.enqueue(10, 2);
        pq.enqueue(20, 5);
        pq.enqueue(30, 1);
        pq.enqueue(40, 4);


        System.out.println("Priority Queue:");

        pq.display();


        // Peek
        System.out.println(
            "\nHighest Priority: "
            + pq.peek()
        );


        // Dequeue
        System.out.println(
            "Removed: "
            + pq.dequeue()
        );


        System.out.println(
            "\nAfter Dequeue:"
        );

        pq.display();
    }
}