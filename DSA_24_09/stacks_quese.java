import java.util.Queue;
import java.util.LinkedList;


public class Main{
    public static void main(String[] args){
        Queue<Integer> queue = new LinkedList<>();

    // this is to add the elements 
        queue.offer(10);
        queue.add(10);
    // this is to remove the elements
        queue.remove(10);
        queue.poll(10);

    // this is for looking the front element 
        queue.element(10);
        queue.peek(10);   
    }
}