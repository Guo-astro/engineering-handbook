// LC 150. Evaluate Reverse Polish Notation
import java.util.ArrayDeque;
import java.util.Deque;

public final class Sol {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (String t : tokens) {
            if (t.length() == 1 && "+-*/".indexOf(t.charAt(0)) >= 0) {
                int b = stack.pop();
                int a = stack.pop();
                switch (t.charAt(0)) {
                    case '+': stack.push(a + b); break;
                    case '-': stack.push(a - b); break;
                    case '*': stack.push(a * b); break;
                    // Java int / int truncates toward zero, matching LC 150 directly.
                    default:  stack.push(a / b); break;
                }
            } else {
                stack.push(Integer.parseInt(t));
            }
        }
        return stack.peek();
    }
}
