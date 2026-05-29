// LC 227. Basic Calculator II
import java.util.ArrayDeque;
import java.util.Deque;

public final class Sol {
    public int calculate(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        int num = 0;
        char op = '+';
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) num = num * 10 + (ch - '0');
            boolean isLast = (i == n - 1);
            if ((!Character.isDigit(ch) && ch != ' ') || isLast) {
                if      (op == '+') stack.push(num);
                else if (op == '-') stack.push(-num);
                else if (op == '*') stack.push(stack.pop() * num);
                // Java int division truncates toward zero.
                else                stack.push(stack.pop() / num);
                num = 0;
                op = ch;
            }
        }
        int total = 0;
        for (int v : stack) total += v;
        return total;
    }
}
