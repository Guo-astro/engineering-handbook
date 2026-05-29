// LC 224. Basic Calculator
import java.util.ArrayDeque;
import java.util.Deque;

public final class Sol {
    public int calculate(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        int result = 0, num = 0, sign = 1;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {
                num = num * 10 + (ch - '0');
            } else if (ch == '+') {
                result += sign * num; num = 0; sign = 1;
            } else if (ch == '-') {
                result += sign * num; num = 0; sign = -1;
            } else if (ch == '(') {
                stack.push(result); stack.push(sign);
                result = 0; sign = 1;
            } else if (ch == ')') {
                result += sign * num; num = 0;
                result *= stack.pop();    // saved sign
                result += stack.pop();    // saved running result
            }
            // whitespace: skip
        }
        result += sign * num;
        return result;
    }
}
