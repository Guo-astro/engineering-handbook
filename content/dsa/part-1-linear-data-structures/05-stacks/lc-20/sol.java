// LC 20. Valid Parentheses
// Push openers; on a closer, peek the top opener and pop iff it matches.
// Keying the pair table by closer keeps the lookup branch-free. The
// terminal stack-empty check rejects unmatched openers.
//
// ArrayDeque is the canonical Java stack: java.util.Stack inherits Vector's
// synchronized methods and is discouraged in modern code. O(n), O(n).
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public final class Sol {

    public static boolean isValid(String s) {
        Map<Character, Character> pair = new HashMap<>();
        pair.put(')', '('); pair.put(']', '['); pair.put('}', '{');
        Deque<Character> stack = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty() || stack.peek() != pair.get(c)) return false;
                stack.pop();
            }
        }
        return stack.isEmpty();
    }

    private Sol() {}
}
