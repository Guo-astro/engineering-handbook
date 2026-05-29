// LC 622. Design Circular Queue
// Fixed-capacity ring buffer. head and tail advance modulo cap; an explicit
// count distinguishes empty (count == 0) from full (count == cap), which
// pure modular indexing alone cannot. All operations O(1), O(k) space.
public class MyCircularQueue {
    private final int[] buf;
    private final int cap;
    private int head;
    private int tail;
    private int count;

    public MyCircularQueue(int k) {
        this.buf = new int[k];
        this.cap = k;
        this.head = 0;
        this.tail = 0;
        this.count = 0;
    }

    public boolean enQueue(int value) {
        if (count == cap) return false;
        buf[tail] = value;
        tail = (tail + 1) % cap;
        count++;
        return true;
    }

    public boolean deQueue() {
        if (count == 0) return false;
        head = (head + 1) % cap;
        count--;
        return true;
    }

    public int Front() {
        return count == 0 ? -1 : buf[head];
    }

    public int Rear() {
        // Java's % can return negative for negative dividends, so add cap
        // before taking the modulus to handle the tail == 0 wrap case.
        return count == 0 ? -1 : buf[(tail - 1 + cap) % cap];
    }

    public boolean isEmpty() {
        return count == 0;
    }

    public boolean isFull() {
        return count == cap;
    }
}
