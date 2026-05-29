// LC 232. Implement Queue using Stacks
import java.util.ArrayDeque;
import java.util.Deque;

public final class Sol {

    /** LC 232. Two ArrayDeques composed as inbox/outbox; amortized O(1) per op.
     *  Use ArrayDeque, not java.util.Stack: Stack extends Vector and synchronizes
     *  every operation. ArrayDeque does not, and Oracle's own JDK 21 docs
     *  recommend it over Stack for stack workloads. */
    public static final class MyQueue {
        private final Deque<Integer> inbox  = new ArrayDeque<>();
        private final Deque<Integer> outbox = new ArrayDeque<>();

        public MyQueue() { }

        public void push(int x) {
            inbox.push(x);                 // O(1) always
        }

        private void transfer() {
            while (!inbox.isEmpty()) {
                outbox.push(inbox.pop());
            }
        }

        public int pop() {
            if (outbox.isEmpty()) transfer();
            return outbox.pop();            // O(1) amortized
        }

        public int peek() {
            if (outbox.isEmpty()) transfer();
            return outbox.peek();           // O(1) amortized
        }

        public boolean empty() {
            return inbox.isEmpty() && outbox.isEmpty();
        }
    }

    private Sol() {}
}
