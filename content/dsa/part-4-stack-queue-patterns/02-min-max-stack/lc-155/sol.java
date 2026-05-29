// LC 155. Min Stack
import java.util.ArrayDeque;
import java.util.Deque;

public final class Sol {

    /** LC 155 Min Stack: ArrayDeque, never java.util.Stack (synchronized Vector subclass). */
    public static final class MinStack {
        private final Deque<Integer> values = new ArrayDeque<>();
        private final Deque<Integer> mins = new ArrayDeque<>();

        public MinStack() {}

        public void push(int val) {
            values.push(val);
            int current = mins.isEmpty() ? val : Math.min(mins.peek(), val);
            mins.push(current);
        }

        public void pop() {
            values.pop();
            mins.pop();
        }

        public int top() {
            return values.peek();
        }

        public int getMin() {
            return mins.peek();
        }
    }

    private Sol() {}
}
